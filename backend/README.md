# AI Chat Backend (Flask)

Production-grade modular backend for authenticated text and image chat.

## Features
- JWT authentication with Redis token blacklist
- Thin Flask routes with service-layer business logic
- Multimodal chat (`text`, `image`, or both)
- Image preprocessing (224x224) and VLM inference path
- MongoDB as primary persistence
- SQLite fallback at `/app/data/<db_name>.db`
- Dockerized deployment with Redis + MongoDB

## Folder Structure
- `app/routes`: HTTP endpoints only
- `app/services`: business logic and integrations
- `app/middleware`: auth middleware
- `models`: local ML models
- `data`: SQLite volume mount directory
- `uploads`: uploaded image storage

## API
### `POST /auth/signup`
Body:
```json
{"email": "user@example.com", "password": "password123"}
```

### `POST /auth/login`
Body:
```json
{"email": "user@example.com", "password": "password123"}
```

### `POST /auth/logout`
Header: `Authorization: Bearer <token>`

### `POST /chat`
Header: `Authorization: Bearer <token>`

Multipart fields:
- `chat_id` (required)
- `text` (optional)
- `image` (optional, field name must be `image`)

If image is provided without text, backend uses default prompt:
`What is this food?`

## Run Locally
1. Copy `.env.example` to `.env`
2. Start stack:
```bash
docker compose up --build
```

Backend: `http://localhost:8000`

## Flutter Camera Contract
For camera capture flow in Flutter:
- Capture image with `camera` plugin
- Compress image
- Send immediately to `POST /chat` as multipart
- Use field name `image`
- Include `chat_id`
- Optionally include `text`, otherwise backend defaults to `What is this food?`
