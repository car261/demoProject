from datetime import datetime, timezone
import logging
import threading
from typing import Any

import redis
from flask import current_app
from pymongo import MongoClient
from pymongo.errors import PyMongoError

from app.services.sqlite_service import SQLiteService


logger = logging.getLogger(__name__)

_shared_mongo_clients: dict[str, MongoClient] = {}
_shared_redis_clients: dict[str, Any] = {}
_client_lock = threading.Lock()


class DatabaseService:
    def __init__(self):
        self._mongo_uri = current_app.config["MONGO_URI"]
        self._redis_url = current_app.config["REDIS_URL"]
        self._sqlite = SQLiteService(
            base_path=current_app.config["SQLITE_BASE_PATH"],
            db_name=current_app.config["SQLITE_DB_NAME"],
        )

    @property
    def mongo_client(self):
        client = _shared_mongo_clients.get(self._mongo_uri)
        if client is None:
            with _client_lock:
                client = _shared_mongo_clients.get(self._mongo_uri)
                if client is None:
                    client = MongoClient(self._mongo_uri, serverSelectionTimeoutMS=3000)
                    _shared_mongo_clients[self._mongo_uri] = client
        return client

    @property
    def redis_client(self):
        client = _shared_redis_clients.get(self._redis_url)
        if client is None:
            with _client_lock:
                client = _shared_redis_clients.get(self._redis_url)
                if client is None:
                    client = redis.from_url(self._redis_url, decode_responses=True)
                    _shared_redis_clients[self._redis_url] = client
        return client

    @property
    def mongo_db(self):
        return self.mongo_client[current_app.config["MONGO_DB_NAME"]]

    def _utc_now(self) -> str:
        return datetime.now(timezone.utc).isoformat()

    def get_user_by_email(self, email: str) -> dict[str, Any] | None:
        try:
            user = self.mongo_db.users.find_one({"email": email})
            if not user:
                return self._sqlite.get_user_by_email(email)
            return {
                "user_id": str(user["_id"]),
                "email": user["email"],
                "password_hash": user["password_hash"],
                "created_at": user.get("created_at"),
            }
        except PyMongoError:
            logger.warning("Mongo unavailable in get_user_by_email, using SQLite fallback")
            return self._sqlite.get_user_by_email(email)

    def create_user(self, user_id: str, email: str, password_hash: str) -> None:
        doc = {
            "_id": user_id,
            "email": email,
            "password_hash": password_hash,
            "created_at": self._utc_now(),
        }
        try:
            self.mongo_db.users.insert_one(doc)
        except PyMongoError:
            logger.warning("Mongo unavailable in create_user, using SQLite fallback")
            self._sqlite.save_user(user_id=user_id, email=email, password_hash=password_hash)

    def save_chat_exchange(
        self,
        user_id: str,
        chat_id: str,
        user_text: str | None,
        assistant_text: str,
        image_path: str | None,
    ) -> None:
        now = self._utc_now()
        user_msg = {
            "user_id": user_id,
            "chat_id": chat_id,
            "role": "user",
            "content": user_text,
            "image_path": image_path,
            "created_at": now,
        }
        assistant_msg = {
            "user_id": user_id,
            "chat_id": chat_id,
            "role": "assistant",
            "content": assistant_text,
            "image_path": None,
            "created_at": now,
        }

        try:
            self.mongo_db.chat_messages.insert_many([user_msg, assistant_msg])
        except PyMongoError:
            logger.warning("Mongo unavailable in save_chat_exchange, using SQLite fallback")
            self._sqlite.save_chat_message(user_id, chat_id, "user", user_text, image_path=image_path)
            self._sqlite.save_chat_message(user_id, chat_id, "assistant", assistant_text, image_path=None)
