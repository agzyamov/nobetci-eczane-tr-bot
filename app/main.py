import os
print("RAILWAY WORKDIR:", os.getcwd())

from fastapi import FastAPI, Request
from bot import bot, dp, WEBHOOK_URL

app = FastAPI()
print("✅ FastAPI app initialized")

@app.on_event("startup")
async def on_startup():
    await bot.set_webhook(WEBHOOK_URL)

@app.on_event("shutdown")
async def on_shutdown():
    await bot.delete_webhook()

@app.post("/")
async def handle_webhook(request: Request):
    body = await request.body()
    print("📩 Incoming webhook data:", body)
    await dp.feed_raw_update(body, bot)
    return {"ok": True}

@app.get("/")
def healthcheck():
    return {"status": "ok"}
