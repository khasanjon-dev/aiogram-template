from aiogram import Router, types
from aiogram.filters import CommandStart

start = Router()


@start.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(f'Hello {message.from_user.first_name}')
