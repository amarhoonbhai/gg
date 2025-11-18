# handlers/__init__.py

from aiogram import Dispatcher

from .user.start import router as user_start_router


def register_all_handlers(dp: Dispatcher) -> None:
    """
    Register all routers/handlers here.
    We'll add admin routers later.
    """
    dp.include_router(user_start_router)
