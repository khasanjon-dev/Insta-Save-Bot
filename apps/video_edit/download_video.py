import os
import re

from dotenv import load_dotenv
from instaloader import Instaloader, Profile

load_dotenv('../../.env')
USERNAME = os.getenv('USERNAME_INSTA')


def download_latest_video(username):
    insta = Instaloader()
    profile = Profile.from_username(insta.context, username)
    posts = profile.get_posts()
    latest_post = next(posts, None)
    while latest_post and not latest_post.is_video:
        latest_post = next(posts, None)
    if latest_post:
        insta.download_post(latest_post, target='today')
        print('Downloaded!')
    else:
        print('No videos found.')


def is_valid_instagram_link(link):
    pattern = r'^https?://(www\.)?instagram\.com/p/[^/]+/?$'
    return re.match(pattern, link)


def handle_input(input_value):
    if is_valid_instagram_link(input_value):
        # Extract the username from the link
        username = input_value.split('/')[-2]
        download_latest_video(username)
    else:
        download_latest_video(input_value)


# Prompt the user for input
input_value = input('Enter an Instagram username or video link: ')
handle_input(input_value)
