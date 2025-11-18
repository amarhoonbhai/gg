# db/base.py

from typing import Optional

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

_client: Optional[MongoClient] = None
_db: Optional[Database] = None


async def init_db(mongo_uri: str, db_name: str) -> None:
    """
    Initialize global Mongo client & DB.
    Called once from bot.py before polling.
    """
    global _client, _db
    _client = MongoClient(mongo_uri)
    _db = _client[db_name]


def get_db() -> Database:
    if _db is None:
        raise RuntimeError("DB not initialized. Call init_db() first.")
    return _db


def get_collection(name: str) -> Collection:
    return get_db()[name]
