import logging

from flask import current_app

from app.services.db import DatabaseService
from app.services.demo_ai import DemoAIService
from app.services.pipeline_service import process_request
from app.services.vlm_service import VLMService


logger = logging.getLogger(__name__)

_shared_db_service = None
_shared_demo_ai = None
_shared_vlm = None
_shared_vlm_key = None


def _get_shared_db_service() -> DatabaseService:
    global _shared_db_service
    if _shared_db_service is None:
        _shared_db_service = DatabaseService()
    return _shared_db_service


def _get_shared_demo_ai() -> DemoAIService:
    global _shared_demo_ai
    if _shared_demo_ai is None:
        _shared_demo_ai = DemoAIService()
    return _shared_demo_ai


def _get_shared_vlm() -> VLMService:
    global _shared_vlm, _shared_vlm_key
    config_key = (current_app.config["MODELS_DIR"], current_app.config["VLM_MODEL_NAME"])
    if _shared_vlm is None or _shared_vlm_key != config_key:
        _shared_vlm = VLMService(models_dir=config_key[0], model_name=config_key[1])
        _shared_vlm_key = config_key
    return _shared_vlm


class ChatAIService:
    def __init__(self):
        self.db = _get_shared_db_service()
        self.demo_ai = _get_shared_demo_ai()
        self.vlm = _get_shared_vlm()

    def generate_reply(self, user_id: str, chat_id: str, text: str | None, image_path: str | None):
        if not isinstance(user_id, str) or not user_id.strip():
            logger.warning("generate_reply called with invalid user_id")
            raise ValueError("user_id is required")

        if not isinstance(chat_id, str) or not chat_id.strip():
            logger.warning("generate_reply called with invalid chat_id")
            raise ValueError("chat_id is required")

        if text is not None and not isinstance(text, str):
            text = str(text)

        if image_path is not None and not isinstance(image_path, str):
            image_path = None

        pipeline_result = process_request(text=text, image_file=image_path)

        assistant_text = None
        if isinstance(pipeline_result, dict):
            answers = pipeline_result.get("answers")
            if isinstance(answers, dict) and answers:
                first_value = next(iter(answers.values()))
                if isinstance(first_value, dict):
                    assistant_text = first_value.get("answer") or first_value.get("reason")
                elif first_value is not None:
                    assistant_text = str(first_value)

            if not assistant_text:
                assistant_text = pipeline_result.get("response")

            if not assistant_text:
                health = pipeline_result.get("health_analysis")
                if isinstance(health, dict):
                    score = health.get("score")
                    if score is not None:
                        assistant_text = f"Health score: {score}/10"

        if not assistant_text:
            if image_path:
                prompt = text or "What is this food?"
                assistant_text = self.vlm.analyze_image(image_path=image_path, prompt=prompt)
            else:
                assistant_text = self.demo_ai.generate_response(text or "")

        self.db.save_chat_exchange(
            user_id=user_id,
            chat_id=chat_id,
            user_text=text,
            assistant_text=assistant_text,
            image_path=image_path,
        )
        return assistant_text
