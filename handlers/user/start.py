# handlers/user/start.py

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

router = Router(name="user_start")


WELCOME_TEXT = (
    "👋 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 <b>𝗖𝗟𝗔𝗦𝗛𝗘𝗥 ❋ 𝗚𝗚 𝗕𝗢𝗧</b>\n\n"
    "I’m your ⚔️ <b>all-in-one Telegram guardian</b> for groups & channels.\n\n"
    "✦ 🔒 Auto-locks & anti-spam\n"
    "✦ 📢 Forced join & invite rules\n"
    "✦ 🌙 Auto Night Mode\n"
    "✦ 🤖 Anti ad-bots & spammers\n"
    "✦ 🏆 Chat leaderboards (all-time / weekly / monthly)\n"
    "✦ 🧩 Multi-chat control – add any group or channel and choose where to enforce rules\n\n"
    "➤ <b>How to set me up:</b>\n"
    "1️⃣ Add me to your <b>group or channel</b>\n"
    "2️⃣ Make me <b>Admin</b> with proper rights\n"
    "3️⃣ Use <code>/panel</code> (soon) to configure locks, joins & punishments\n\n"
    "Let’s see who really dominates the chat. 🏹🔥"
)


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer(WELCOME_TEXT)
