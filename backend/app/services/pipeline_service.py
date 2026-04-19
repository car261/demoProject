import logging
import os
import re
from typing import Any

from app.services.ocr_service import run_ocr


logger = logging.getLogger(__name__)


def _empty_nutrition() -> dict[str, str]:
    return {
        "calories": "Not found",
        "protein": "Not found",
        "carbs": "Not found",
        "fat": "Not found",
        "sodium": "Not found",
        "fiber": "Not found",
        "sugar": "Not found",
    }


def _parse_from_ocr_text(text: str) -> dict[str, str]:
    data = _empty_nutrition()
    patterns = {
        "calories": r"calories?\s*[:]?\s*(\d+(?:\.\d+)?)",
        "protein": r"protein\s*[:]?\s*(\d+(?:\.\d+)?)\s*g?",
        "carbs": r"carbs?|carbohydrates?\s*[:]?\s*(\d+(?:\.\d+)?)\s*g?",
        "fat": r"fat\s*[:]?\s*(\d+(?:\.\d+)?)\s*g?",
        "sodium": r"sodium\s*[:]?\s*(\d+(?:\.\d+)?)\s*mg?",
        "fiber": r"fiber\s*[:]?\s*(\d+(?:\.\d+)?)\s*g?",
        "sugar": r"sugars?\s*[:]?\s*(\d+(?:\.\d+)?)\s*g?",
    }

    lower_text = text.lower()
    for key, pattern in patterns.items():
        match = re.search(pattern, lower_text)
        if match:
            value = match.group(1)
            if key == "calories":
                data[key] = f"{value} kcal"
            elif key == "sodium":
                data[key] = f"{value} mg"
            else:
                data[key] = f"{value} g"

    return data


def extract_from_image(image_file: Any) -> dict[str, str]:
    """Extract nutrition-like fields from an image path or file object.

    Falls back to an empty nutrition schema if OCR is unavailable.
    """
    try:
        image_path = None
        if isinstance(image_file, str):
            image_path = image_file
        elif hasattr(image_file, "filename") and getattr(image_file, "filename", None):
            image_path = image_file.filename

        if not image_path or not os.path.exists(image_path):
            return _empty_nutrition()

        try:
            import pytesseract
            from PIL import Image
        except Exception:
            logger.warning("pytesseract not installed; using empty OCR fallback")
            return _empty_nutrition()

        text = pytesseract.image_to_string(Image.open(image_path))
        if not text.strip():
            return _empty_nutrition()

        return _parse_from_ocr_text(text)
    except Exception:
        logger.exception("OCR extraction failed")
        return _empty_nutrition()


def process_request(text: str | None, image_file):
    if image_file:
        nutrition_data = extract_from_image(image_file)
        questions = [text] if text and text.strip() else []
        return run_ocr(nutrition_data, questions)

    if text and text.strip():
        return run_ocr({}, [text])

    return {"response": "Invalid input"}
