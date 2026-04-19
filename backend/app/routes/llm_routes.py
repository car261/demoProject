import os
import uuid
from pathlib import Path

from flask import Blueprint, current_app, g, request
from werkzeug.utils import secure_filename

from app.middleware.auth_middleware import token_required
from app.services.chat_ai import ChatAIService
from app.services.response import error_response, success_response


llm_bp = Blueprint("llm", __name__)


def _allowed_file(filename: str) -> bool:
    ext = Path(filename).suffix.lower().replace(".", "")
    return ext in current_app.config["ALLOWED_IMAGE_EXTENSIONS"]


@llm_bp.post("/chat")
@token_required
def chat():
    content_type = request.content_type or ""
    is_multipart = "multipart/form-data" in content_type

    if is_multipart:
        text = request.form.get("text")
        chat_id = request.form.get("chat_id")
        image = request.files.get("image") or request.files.get("file")
    else:
        payload = request.get_json(silent=True) or {}
        text = payload.get("text")
        chat_id = payload.get("chat_id")
        image = None

    chat_id = (chat_id or "").strip()
    if not chat_id:
        return error_response("chat_id is required", 400, "VALIDATION_ERROR")

    if not text and not image:
        return error_response("Either text or image is required", 400, "VALIDATION_ERROR")

    image_path = None
    if image:
        filename = secure_filename(image.filename or "")
        if not filename or not _allowed_file(filename):
            return error_response("Invalid image file", 400, "INVALID_FILE")

        if image.mimetype and not image.mimetype.startswith("image/"):
            return error_response("Invalid file type", 400, "INVALID_FILE")

        upload_dir = os.path.join(current_app.config["UPLOAD_FOLDER"], chat_id)
        os.makedirs(upload_dir, exist_ok=True)

        file_ext = Path(filename).suffix.lower()
        generated_name = f"{uuid.uuid4().hex}{file_ext}"
        image_path = os.path.join(upload_dir, generated_name)
        image.save(image_path)

        if not text:
            text = "What is this food?"

    service = ChatAIService()
    assistant_text = service.generate_reply(
        user_id=g.current_user["user_id"],
        chat_id=chat_id,
        text=text,
        image_path=image_path,
    )

    return success_response(
        "Chat processed successfully",
        {
            "chat_id": chat_id,
            "response": assistant_text,
            "used_image": bool(image_path),
        },
        200,
    )
