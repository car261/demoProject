import uuid

import bcrypt

from app.services.db import DatabaseService


class AuthService:
    def __init__(self):
        self.db = DatabaseService()

    def signup(self, email: str, password: str):
        existing = self.db.get_user_by_email(email)
        if existing:
            raise ValueError("Email already exists")

        password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        user_id = str(uuid.uuid4())
        self.db.create_user(user_id=user_id, email=email, password_hash=password_hash)
        return {"user_id": user_id, "email": email}

    def login(self, email: str, password: str):
        user = self.db.get_user_by_email(email)
        if not user:
            raise ValueError("Invalid credentials")

        valid = bcrypt.checkpw(password.encode("utf-8"), user["password_hash"].encode("utf-8"))
        if not valid:
            raise ValueError("Invalid credentials")

        return user
