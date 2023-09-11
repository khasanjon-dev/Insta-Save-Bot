from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from loader import dp, bot
from utils.db_api.queries import db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user = message.from_user
    if user.language_code == 'uz':
        await message.answer(f"Assalomu alaykum, {user.first_name}!")
        await message.answer(
            'Instagramdan surat yoki videolarni yuklab olishingiz mumkin \nShunchaki havolani yuboring)')
    elif user.language_code == 'en':
        await message.answer(f"Hello, {message.from_user.first_name}!")
        await message.answer('You can download photos or videos from Instagram \nJust send the link)')
    elif user.language_code == 'ru':
        await message.answer(f"Привет, {message.from_user.first_name}!")
        await message.answer('Вы можете скачать фото или видео из Инстаграм\nПросто пришлите ссылку)')
    data = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.username,
        'telegram_id': user.id,
        'language_code': user.language_code
    }
    await db.create_or_update(data)
    for admin in ADMINS:
        count = await db.count_users()
        text = f'{user.first_name}\n@{user.username} added!\nAll members count {count}'
        await bot.send_message(admin, text)
