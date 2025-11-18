# handlers/admin/addchat.py

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from db.chats import link_chat, unlink_chat

router = Router(name="admin_addchat")


async def _is_admin(message: Message) -> bool:
    """
    Simple admin check using get_chat_member.
    Works for groups/channels, not private.
    """
    if message.chat.type == "private":
        return False

    member = await message.bot.get_chat_member(
        message.chat.id,
        message.from_user.id,
    )
    return member.status in {"administrator", "creator"}


@router.message(Command("addchat"))
async def cmd_addchat(message: Message) -> None:
    # Only work in groups/channels
    if message.chat.type == "private":
        await message.answer("❌ Use /addchat inside a group or channel.")
        return

    if not await _is_admin(message):
        await message.answer("❌ Only chat admins can use /addchat.")
        return

    doc = link_chat(
        chat_id=message.chat.id,
        title=message.chat.title or "<no title>",
        chat_type=message.chat.type,  # "group", "supergroup", "channel"
    )

    await message.answer(
        f"✅ <b>Chat linked to ClasherGG.</b>\n"
        f"ID: <code>{message.chat.id}</code>\n"
        f"Title: <b>{doc.get('title', '')}</b>"
    )


@router.message(Command("delchat"))
async def cmd_delchat(message: Message) -> None:
    if message.chat.type == "private":
        await message.answer("❌ Use /delchat inside the group or channel you want to unlink.")
        return

    if not await _is_admin(message):
        await message.answer("❌ Only chat admins can use /delchat.")
        return

    ok = unlink_chat(message.chat.id)
    if ok:
        await message.answer("✅ This chat has been <b>unlinked</b> from ClasherGG.")
    else:
        await message.answer("ℹ️ This chat was not linked or was already removed.")
