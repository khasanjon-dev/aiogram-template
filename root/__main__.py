"""This file represent startup bot logic."""
import asyncio
import logging

from aiogram.fsm.storage.memory import MemoryStorage

from utils.set_bot_commands import set_default_commands
from .dispatcher import get_dispatcher
from .settings import settings, bot


async def start_bot():
    """This function will start bot with polling mode."""

    # storage = get_redis_storage(
    #     redis=Redis(
    #         db=settings.redis.db,
    #         host=settings.redis.host,
    #         password=settings.redis.passwd,
    #         username=settings.redis.username,
    #         port=settings.redis.port,
    #     )
    # )
    dp = get_dispatcher(storage=MemoryStorage())
    await set_default_commands(bot)
    await dp.start_polling(
        bot,
        allowed_updates=dp.resolve_used_update_types()
    )


if __name__ == '__main__':
    logging.basicConfig(level=settings.logging_level)
    asyncio.run(start_bot())
