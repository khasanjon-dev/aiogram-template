"""This file represents configurations from files and environment."""
import logging
import os
from dataclasses import dataclass

from aiogram import Bot
from dotenv import load_dotenv

load_dotenv()


@dataclass
class RedisConfig:
    """Redis connection variables."""

    db: int = int(os.getenv('REDIS_DATABASE', 1))
    """ Redis Database ID """
    host: str = os.getenv('REDIS_HOST', 'redis')
    port: int = int(os.getenv('REDIS_PORT', 6379))
    passwd: str | None = os.getenv('REDIS_PASSWORD')
    username: str | None = os.getenv('REDIS_USERNAME')
    state_ttl: int | None = os.getenv('REDIS_TTL_STATE', None)
    data_ttl: int | None = os.getenv('REDIS_TTL_DATA', None)


@dataclass
class BotConfig:
    """Bot configuration."""

    token: str = os.getenv('BOT_TOKEN')
    base_path: str = os.getenv('BASE_PATH')
    BASE_URL: str = os.getenv('BASE_URL')


@dataclass
class Configuration:
    """All in one configuration's class."""

    debug = bool(os.getenv('DEBUG'))
    logging_level = int(os.getenv('LOGGING_LEVEL', logging.INFO))

    redis = RedisConfig()
    bot = BotConfig()


class Settings(Configuration):
    base_url: str = os.getenv('BASE_URL')


settings = Settings()
bot = Bot(token=settings.bot.token)