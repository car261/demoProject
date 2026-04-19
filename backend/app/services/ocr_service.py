import logging

from models.core.inference import run_inference


logger = logging.getLogger(__name__)

def run_ocr(nutrition_data: dict, questions: list[str]):
    if not isinstance(nutrition_data, dict):
        logger.warning("run_ocr called with non-dict nutrition_data")
        nutrition_data = {}

    if questions is None:
        questions = []
    elif not isinstance(questions, list):
        logger.warning("run_ocr called with non-list questions")
        questions = []

    return run_inference(nutrition_data, questions)