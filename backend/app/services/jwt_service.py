import uuid
import logging
from datetime import datetime, timedelta, timezone

import jwt
from flask import current_app


logger = logging.getLogger(__name__)


class JWTService:
    def __init__(self, redis_client=None):
        self.redis_client = redis_client

    def generate_token(self, user_id: str, email: str) -> str:
        now = datetime.now(timezone.utc)
        exp = now + timedelta(minutes=current_app.config["JWT_EXP_MINUTES"])
        jti = str(uuid.uuid4())

        payload = {
            "sub": user_id,
            "email": email,
            "jti": jti,
            "iat": int(now.timestamp()),
            "exp": int(exp.timestamp()),
        }

        return jwt.encode(payload, current_app.config["JWT_SECRET"], algorithm=current_app.config["JWT_ALGORITHM"])

    def decode_token(self, token: str):
        payload = jwt.decode(
            token,
            current_app.config["JWT_SECRET"],
            algorithms=[current_app.config["JWT_ALGORITHM"]],
        )

        jti = payload.get("jti")
        if jti and self.redis_client:
            try:
                if self.redis_client.get(f"blacklist:{jti}"):
                    raise jwt.InvalidTokenError("Token has been revoked")
            except Exception as exc:
                logger.warning("Redis unavailable during token blacklist check: %s", exc)
                # Token is still valid if JWT signature checks out.
                pass

        return payload

    def blacklist_token(self, token: str) -> None:
        payload = jwt.decode(
            token,
            current_app.config["JWT_SECRET"],
            algorithms=[current_app.config["JWT_ALGORITHM"]],
            options={"verify_exp": False},
        )
        jti = payload.get("jti")
        exp = payload.get("exp")
        if not jti or not exp or not self.redis_client:
            return

        now_ts = int(datetime.now(timezone.utc).timestamp())
        ttl = max(exp - now_ts, 1)
        try:
            self.redis_client.setex(f"blacklist:{jti}", ttl, "1")
        except Exception as exc:
            logger.warning("Redis unavailable during token blacklist write: %s", exc)
