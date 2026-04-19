from datetime import datetime


class DemoAIService:
    def generate_response(self, text: str) -> str:
        normalized = (text or "").strip().lower()

        if any(word in normalized for word in ["hello", "hi", "hey"]):
            return "Hello. How can I help you today?"
        if "food" in normalized:
            return "This looks like a food-related request. Share more details and I can help with nutrition, recipe ideas, or quick analysis."
        if "time" in normalized:
            return f"Current server time is {datetime.utcnow().isoformat()}Z"

        return f"Demo AI response: {text}"
