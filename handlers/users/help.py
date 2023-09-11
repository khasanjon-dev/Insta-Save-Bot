from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    user = message.from_user
    text = ''
    if user.language_code == 'uz':
        text = "Shunchaki instagram havolasini yuboring 🫠!"
    elif user.language_code == 'en':
        text = "Just send instagram link 🫠 !"
    elif user.language_code == 'ru':
        text = "Просто пришлите ссылку в инстаграм 🫠!"
    await message.answer(text)
