import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message
from aiogram.filters import Command

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

if BOT_TOKEN is None:
    raise ValueError("BOT_TOKEN environment variable is not set")

bot = Bot(token=BOT_TOKEN)
router = Router()

@router.message(Command("start"))
async def handle_start(msg: Message):
    await msg.answer("Привет! Я помогу найти дежурные аптеки в Турции 🏥")

dp = Dispatcher()
dp.include_router(router)
