import os
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone


class SQLiteService:
    def __init__(self, base_path: str, db_name: str):
        self.base_path = base_path
        self.db_name = db_name
        self.db_path = self._build_db_path(base_path, db_name)
        self._initialize()

    @staticmethod
    def _build_db_path(base_path: str, db_name: str) -> str:
        safe_name = db_name.replace(".db", "")
        root = (base_path or "").strip()
        if not root:
            root = "/app/data"

        root = os.path.normpath(root)
        os.makedirs(root, exist_ok=True)
        return os.path.join(root, f"{safe_name}.db")

    @contextmanager
    def _connection(self):
        conn = sqlite3.connect(self.db_path)
        try:
            yield conn
        finally:
            conn.close()

    def _initialize(self) -> None:
        with self._connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT UNIQUE NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
                """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS chat_messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT NOT NULL,
                    chat_id TEXT NOT NULL,
                    role TEXT NOT NULL,
                    content TEXT,
                    image_path TEXT,
                    created_at TEXT NOT NULL
                )
                """
            )
            conn.commit()

    def save_user(self, user_id: str, email: str, password_hash: str) -> None:
        created_at = datetime.now(timezone.utc).isoformat()
        with self._connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO users (user_id, email, password_hash, created_at)
                VALUES (?, ?, ?, ?)
                """,
                (user_id, email, password_hash, created_at),
            )
            conn.commit()

    def get_user_by_email(self, email: str):
        with self._connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT user_id, email, password_hash, created_at
                FROM users
                WHERE email = ?
                LIMIT 1
                """,
                (email,),
            )
            row = cursor.fetchone()

        if not row:
            return None

        return {
            "user_id": row[0],
            "email": row[1],
            "password_hash": row[2],
            "created_at": row[3],
        }

    def save_chat_message(self, user_id: str, chat_id: str, role: str, content: str | None, image_path: str | None = None) -> None:
        created_at = datetime.now(timezone.utc).isoformat()
        with self._connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO chat_messages (user_id, chat_id, role, content, image_path, created_at)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (user_id, chat_id, role, content, image_path, created_at),
            )
            conn.commit()
