from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from utils.db_api.queries import db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Hello, {message.from_user.first_name}!")
    await message.answer(f"You can download photos or videos from Instagram \nJust send the link)")
    user = message.from_user
    data = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.username,
        'telegram_id': user.id
    }
    db.create_or_update(data)
