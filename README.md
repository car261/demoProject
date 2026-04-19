# Full-Stack OCR + LLM Chat System

Production-ready full-stack application with Flutter frontend and Flask backend.

Architecture:
Flutter -> Flask API -> OCR pipeline -> LLM inference -> response

## Project Overview

This project includes:
- Flutter mobile client in lib/
- Flask backend in backend/
- JWT-based authentication
- OCR + inference pipeline for nutrition/image analysis
- Redis-backed token blacklist support with safe fallback when Redis is unavailable

## Architecture

Request flow:
1. Flutter sends text, image, or text+image with Bearer token
2. Flask /chat validates JWT
3. Pipeline service processes request
4. OCR extraction runs for image inputs
5. Inference model executes and returns output
6. Response is returned to Flutter and displayed

## Setup Instructions

### Backend

```bash
cd backend
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env
python run.py
```

Backend runs on http://localhost:8000 by default.

### Flutter

```bash
flutter pub get
flutter run --dart-define=API_BASE_URL=http://10.0.2.2:8000
```

For physical devices, replace the URL with your machine LAN IP.

## API

### POST /chat

Supports:
- JSON text-only
- Multipart image-only
- Multipart text+image

Headers:
- Authorization: Bearer <token>

Example JSON request:

```json
{
	"text": "Is this meal healthy?",
	"chat_id": "default"
}
```

Example successful response envelope:

```json
{
	"success": true,
	"message": "Chat processed successfully",
	"data": {
		"chat_id": "default",
		"response": "...",
		"used_image": true
	}
}
```

## Environment Variables

Use backend/.env.example as reference.

Required:
- FLASK_ENV
- SECRET_KEY
- JWT_SECRET
- REDIS_URL
- MONGO_URI
- MODELS_DIR

## Security Notes

- Do not commit .env files or secrets.
- Redis is optional for auth blacklist checks; auth continues safely if Redis is down.
- Flutter API base URL is configurable through --dart-define.

## Repository Layout

Top-level structure:
- backend/
- lib/
- README.md
- .gitignore

Optional documentation can be added under docs/.
