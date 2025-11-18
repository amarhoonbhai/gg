# db/chats.py

from datetime import datetime
from typing import Optional, Literal, Dict, Any

from .base import get_collection

ChatType = Literal["private", "group", "supergroup", "channel"]


def link_chat(chat_id: int, title: str, chat_type: ChatType) -> Dict[str, Any]:
    """
    Link (register) a chat with ClasherGG.
    Upserts basic settings with safe defaults.
    """
    col = get_collection("chats")
    now = datetime.utcnow()

    doc = col.find_one({"chat_id": chat_id})
    if doc is None:
        doc = {
            "chat_id": chat_id,
            "type": chat_type,
            "title": title,
            "linked_at": now,
            "locks": {
                "links": False,
                "media": False,
                "stickers": False,
                "gifs": False,
                "forwards": False,
                "bots": False,
                "bad_words": False,
            },
            "join_rules": {
                "required_channels": [],
                "force_invite_enabled": False,
                "min_invites": 1,
            },
            "night_mode": {
                "enabled": False,
                "start": "23:00",
                "end": "07:00",
                "action": "lock",
            },
            "punishments": {
                "links": {"type": "mute", "duration_sec": 600},
                "spam": {"type": "ban", "duration_sec": 86400},
                "ads": {"type": "ban", "duration_sec": 604800},
            },
        }
        col.insert_one(doc)
    else:
        col.update_one(
            {"chat_id": chat_id},
            {
                "$set": {
                    "title": title,
                    "type": chat_type,
                    "linked_at": now,
                }
            },
        )
        doc = col.find_one({"chat_id": chat_id})

    return doc


def unlink_chat(chat_id: int) -> bool:
    """
    Unlink (remove) a chat from ClasherGG.
    Returns True if something was deleted.
    """
    col = get_collection("chats")
    result = col.delete_one({"chat_id": chat_id})
    return result.deleted_count > 0


def get_chat(chat_id: int) -> Optional[Dict[str, Any]]:
    """
    Get chat settings doc (or None).
    """
    col = get_collection("chats")
    return col.find_one({"chat_id": chat_id})
