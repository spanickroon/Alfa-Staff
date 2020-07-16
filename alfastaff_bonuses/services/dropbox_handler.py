"""This module contain functions for dropbox storage."""


def get_avatars_from_dropbox(user):
    """If avatar.url not returned image, return default image."""
    try:
        avatar = user.profile.avatar.url
        return avatar
    except:
        avatar = 'static/images/site/anon_user.png'
        return avatar