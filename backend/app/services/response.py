from datetime import datetime, timezone
from flask import jsonify


def _build_payload(success: bool, message: str, data=None, error_code: str | None = None):
    payload = {
        "success": success,
        "message": message,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    if data is not None:
        payload["data"] = data

    if error_code:
        payload["error_code"] = error_code

    return payload


def success_response(message: str, data=None, status_code: int = 200):
    return jsonify(_build_payload(True, message, data=data)), status_code


def error_response(message: str, status_code: int = 400, error_code: str | None = None):
    return jsonify(_build_payload(False, message, error_code=error_code)), status_code
