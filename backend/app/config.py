import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "change-me-in-production")
    JWT_SECRET = os.getenv("JWT_SECRET", "change-me-in-production")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
    JWT_EXP_MINUTES = int(os.getenv("JWT_EXP_MINUTES", "60"))

    MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongodb:27017")
    MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "ai_chat")

    REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")

    SQLITE_BASE_PATH = os.getenv("SQLITE_BASE_PATH", "/app/data")
    SQLITE_DB_NAME = os.getenv("SQLITE_DB_NAME", "chat_local")

    MODELS_DIR = os.getenv("MODELS_DIR", "/app/models")
    VLM_MODEL_NAME = os.getenv("VLM_MODEL_NAME", "nlpconnect/vit-gpt2-image-captioning")

    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "/app/uploads")
    MAX_CONTENT_LENGTH = int(os.getenv("MAX_CONTENT_LENGTH", str(10 * 1024 * 1024)))
    ALLOWED_IMAGE_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}
