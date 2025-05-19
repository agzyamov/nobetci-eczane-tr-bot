# Nöbetçi Eczane Telegram Bot

A Telegram bot built with FastAPI and Aiogram for locating duty pharmacies in Turkey.

## Setup

1. Copy `.env.example` to `.env`
2. Run locally:

```
uvicorn app.main:app --reload
```

3. For deployment:

```
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
