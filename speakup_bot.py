import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import (
    Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, BotCommand
)
from aiogram.filters import Command

BOT_TOKEN = os.getenv("BOT_TOKEN")
SPEAKUP_URL = "https://speakup-rose.vercel.app"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(
            text="🎙 Start Speaking Test",
            web_app=WebAppInfo(url=SPEAKUP_URL)
        )
    ]])
    name = message.from_user.first_name or "there"
    await message.answer(
        f"👋 Hello, {name}!\n\n"
        f"Welcome to *SpeakUP!* — your IELTS Speaking mock test platform by Alisher Abduvohobov.\n\n"
        f"🎯 *What to expect:*\n"
        f"• 3 parts · 12 questions · ~14 minutes (approx.)\n"
        f"• Examiner asks the questions\n"
        f"• Your answers will be automatically recorded\n"
        f"• Instant band score + feedback\n\n"
        f"Find a quiet place and tap the button below when ready. 🎧",
        parse_mode="Markdown",
        reply_markup=keyboard
    )

@dp.message(Command("test"))
async def test_handler(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(
            text="🎙 Start Speaking Test",
            web_app=WebAppInfo(url=SPEAKUP_URL)
        )
    ]])
    await message.answer(
        "Tap below to open your IELTS Speaking test. 👇\n\n"
        "_Make sure you're in a quiet place with your mic ready._",
        parse_mode="Markdown",
        reply_markup=keyboard
    )

@dp.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(
        "*SpeakUP! — Help*\n\n"
        "🎙 /start — Welcome message + open test\n"
        "📝 /test — Open the speaking test directly\n"
        "❓ /help — Show this message\n\n"
        "*How the test works:*\n"
        "1. Enter your access code (given by your teacher)\n"
        "2. The AI examiner asks questions — listen carefully\n"
        "3. Press the mic button and answer each question\n"
        "4. After all 3 parts, get your band score instantly\n\n"
        "If you have issues, contact your teacher directly.",
        parse_mode="Markdown"
    )

async def set_commands():
    await bot.set_my_commands([
        BotCommand(command="start", description="Welcome & open test"),
        BotCommand(command="test", description="Start speaking test"),
        BotCommand(command="help", description="How it works"),
    ])

async def main():
    await set_commands()
    print("SpeakUP! bot is running...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
