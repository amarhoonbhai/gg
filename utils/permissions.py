# utils/permissions.py

from aiogram.types import Message

from config import BOT_CONFIG


async def is_owner(user_id: int) -> bool:
    return user_id in BOT_CONFIG.owner_ids


async def is_admin(message: Message) -> bool:
    """
    True if user is group/channel admin or global owner.
    """
    if message.chat.type == "private":
        return False

    # Owners always pass
    if await is_owner(message.from_user.id):
        return True

    member = await message.bot.get_chat_member(
        message.chat.id,
        message.from_user.id,
    )
    return member.status in {"administrator", "creator"}
