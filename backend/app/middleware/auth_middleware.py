from functools import wraps
import logging

import jwt
from flask import g, request

from app.services.db import DatabaseService
from app.services.jwt_service import JWTService
from app.services.response import error_response


logger = logging.getLogger(__name__)


def token_required(handler):
    @wraps(handler)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            return error_response("Missing or invalid authorization header", 401, "UNAUTHORIZED")

        token = auth_header.split(" ", 1)[1].strip()
        try:
            db = DatabaseService()
            jwt_service = JWTService(redis_client=db.redis_client)
            payload = jwt_service.decode_token(token)
            g.current_user = {
                "user_id": payload["sub"],
                "email": payload.get("email"),
                "jti": payload.get("jti"),
            }
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            logger.warning("Token validation failed")
            return error_response("Unauthorized", 401, "UNAUTHORIZED")
        except Exception:
            logger.exception("Unexpected token validation error")
            return error_response("Unauthorized", 401, "UNAUTHORIZED")

        return handler(*args, **kwargs)

    return wrapper
