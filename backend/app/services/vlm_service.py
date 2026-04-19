import logging
import os
import threading

from PIL import Image


logger = logging.getLogger(__name__)


class VLMService:
    _pipeline_cache = {}
    _cache_lock = threading.Lock()

    def __init__(self, models_dir: str, model_name: str):
        self.models_dir = models_dir
        self.model_name = model_name
        self._pipeline = None

    def _load_pipeline(self):
        if self._pipeline is not None:
            return self._pipeline

        cache_key = (self.models_dir, self.model_name)
        with self._cache_lock:
            cached = self._pipeline_cache.get(cache_key)
            if cached is not None:
                self._pipeline = cached
                return self._pipeline

        try:
            from transformers import pipeline
        except Exception:
            logger.exception("Unable to import transformers pipeline")
            self._pipeline = None
            return None

        try:
            model_path = os.path.join(self.models_dir, self.model_name)
            if os.path.isdir(model_path):
                self._pipeline = pipeline("image-to-text", model=model_path)
            else:
                self._pipeline = pipeline("image-to-text", model=self.model_name)

            with self._cache_lock:
                self._pipeline_cache[cache_key] = self._pipeline
        except Exception:
            logger.exception("Failed to load VLM pipeline")
            self._pipeline = None
        return self._pipeline

    def _preprocess(self, image_path: str):
        # Mandatory preprocessing for image models.
        image = Image.open(image_path).convert("RGB")
        resized = image.resize((224, 224))

        try:
            import numpy as np
            import torch

            arr = np.array(resized).astype("float32") / 255.0
            tensor = torch.from_numpy(arr).permute(2, 0, 1).unsqueeze(0)
            return resized, tensor
        except Exception:
            return resized, None

    def analyze_image(self, image_path: str, prompt: str) -> str:
        if not isinstance(image_path, str) or not image_path.strip():
            logger.warning("analyze_image called with invalid image path")
            return "I could not process this image safely. Please try another image."

        if not os.path.exists(image_path):
            logger.warning("analyze_image path not found: %s", image_path)
            return "I could not process this image safely. Please try another image."

        try:
            processed_image, _ = self._preprocess(image_path)
            model_pipeline = self._load_pipeline()
            if not model_pipeline:
                return "Image received and processed, but vision model is unavailable right now."

            raw = model_pipeline(processed_image)
            if isinstance(raw, list) and raw:
                text = raw[0].get("generated_text", "")
            else:
                text = ""

            if not text:
                return "I processed the image but could not generate a confident description."

            if prompt:
                return f"{text} | Prompt context: {prompt}"
            return text
        except Exception:
            logger.exception("VLM analyze_image failed")
            return "I could not process this image safely. Please try another image."
