import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

if BOT_TOKEN is None:
    raise ValueError("BOT_TOKEN environment variable is not set")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def handle_start(msg: Message):
    await msg.answer("Привет! Я помогу найти дежурные аптеки в Турции 🏥")
