import instaloader


def download_instagram_video(url):
    loader = instaloader.Instaloader()
    try:
        post = instaloader.Post.from_shortcode(loader.context, url.split('/')[-2])
        loader.download_post(post, target='media')
        print("Video downloaded successfully!")
    except instaloader.exceptions.ProfileNotExistsException:
        print("Profile not found.")
    except instaloader.exceptions.PrivateProfileNotFollowedException:
        print("Cannot download videos from private accounts.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


video_url = 'https://www.instagram.com/p/CuePqiwMwmz/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA=='

download_instagram_video(video_url)
