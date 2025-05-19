import os

from fastapi import FastAPI, Request
from aiogram.types import Update
from bot import bot, dp, WEBHOOK_URL

app = FastAPI()
print("✅ FastAPI app initialized")

@app.on_event("startup")
async def on_startup():
    print("✅ Startup triggered")
    await bot.set_webhook(WEBHOOK_URL)

@app.on_event("shutdown")
async def on_shutdown():
    print("👋 Shutdown triggered")
    await bot.delete_webhook()

@app.post("/")
async def handle_webhook(request: Request):
    try:
        data = await request.json()
        print("📩 Incoming webhook JSON:", data)
        update = Update.model_validate(data)
        print("🔄 Dispatching update...")
        await dp.feed_update(bot, update)
    except Exception as e:
        print("❌ Error in handle_webhook:", e)
        return {"ok": False, "error": str(e)}
    return {"ok": True}

@app.get("/")
def healthcheck():
    return {"status": "ok"}
