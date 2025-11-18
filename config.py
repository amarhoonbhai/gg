# config.py

from dataclasses import dataclass
from typing import Set


@dataclass
class BotConfig:
    token: str
    mongo_uri: str
    db_name: str
    owner_ids: Set[int]


# 🔧 EDIT THESE VALUES BEFORE RUNNING

BOT_CONFIG = BotConfig(
    token="PASTE_YOUR_BOT_TOKEN_HERE",          # from @BotFather
    mongo_uri="mongodb://localhost:27017",      # change if using remote Mongo
    db_name="clashergg_bot",                    # database name
    owner_ids={123456789},                      # your Telegram user ID(s)
)
