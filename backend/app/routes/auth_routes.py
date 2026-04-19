from flask import Blueprint, request

from app.middleware.auth_middleware import token_required
from app.services.auth_service import AuthService
from app.services.db import DatabaseService
from app.services.jwt_service import JWTService
from app.services.response import error_response, success_response


auth_bp = Blueprint("auth", __name__)


@auth_bp.post("/signup")
def signup():
    payload = request.get_json(silent=True) or {}
    email = (payload.get("email") or "").strip().lower()
    password = payload.get("password") or ""

    if not email or not password:
        return error_response("Email and password are required", 400, "VALIDATION_ERROR")

    if len(password) < 8:
        return error_response("Password must be at least 8 characters", 400, "VALIDATION_ERROR")

    auth_service = AuthService()
    db = DatabaseService()
    jwt_service = JWTService(redis_client=db.redis_client)

    try:
        user = auth_service.signup(email=email, password=password)
        token = jwt_service.generate_token(user_id=user["user_id"], email=user["email"])
        return success_response("Signup successful", {"token": token, "user": user}, 201)
    except ValueError as exc:
        return error_response(str(exc), 400, "AUTH_ERROR")
    except Exception:
        return error_response("Unable to complete signup", 500, "SERVER_ERROR")


@auth_bp.post("/login")
def login():
    payload = request.get_json(silent=True) or {}
    email = (payload.get("email") or "").strip().lower()
    password = payload.get("password") or ""

    if not email or not password:
        return error_response("Email and password are required", 400, "VALIDATION_ERROR")

    auth_service = AuthService()
    db = DatabaseService()
    jwt_service = JWTService(redis_client=db.redis_client)

    try:
        user = auth_service.login(email=email, password=password)
        token = jwt_service.generate_token(user_id=user["user_id"], email=user["email"])
        return success_response(
            "Login successful",
            {"token": token, "user": {"user_id": user["user_id"], "email": user["email"]}},
        )
    except ValueError:
        return error_response("Invalid credentials", 401, "AUTH_ERROR")
    except Exception:
        return error_response("Unable to complete login", 500, "SERVER_ERROR")


@auth_bp.post("/logout")
@token_required
def logout():
    auth_header = request.headers.get("Authorization", "")
    token = auth_header.split(" ", 1)[1].strip()

    db = DatabaseService()
    jwt_service = JWTService(redis_client=db.redis_client)
    try:
        jwt_service.blacklist_token(token)
        return success_response("Logout successful", status_code=200)
    except Exception:
        return error_response("Unable to logout", 500, "SERVER_ERROR")
