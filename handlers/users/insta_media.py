import re

from aiogram import types
from instaloader import Instaloader, Post

from data.config import BOT_USERNAME
from loader import dp


@dp.message_handler()
async def send_media(message: types.Message):
    url = message.text
    shortcode = extract_shortcode(url)
    if shortcode:
        await message.answer('⏳')
        loader = Instaloader()
        i = 0
        post = Post.from_shortcode(loader.context, shortcode)
        for _post in post.get_sidecar_nodes():
            if _post.is_video:
                video_url = _post.video_url
                await message.answer_video(types.InputFile.from_url(video_url), caption=BOT_USERNAME)
            else:
                photo_url = _post.display_url
                await message.answer_photo(types.InputFile.from_url(photo_url), caption=BOT_USERNAME)
            i += 1
        if i == 0:
            if post.is_video:
                video_url = post.video_url
                await message.answer_video(types.InputFile.from_url(video_url), caption=BOT_USERNAME)
            else:
                photo_url = post.url
                await message.answer_photo(types.InputFile.from_url(photo_url), caption=BOT_USERNAME)
    else:
        await message.reply('Invalid Instagram URL')


def extract_shortcode(url):
    regex = r"(?:instagram\.com\/(?:p|reel)\/|instagr\.am\/(?:p|reel)\/)([\w\-]+)"
    match = re.search(regex, url)
    if match:
        return match.group(1)
    return None
