"""This module contain functions for dropbox storage."""

from base64 import b64encode


def get_avatars_from_avatar_binary(user):
    """Get avatars from avatar binary."""
    avatar = b64encode(user.profile.avatar_binary).decode('ascii')
    return avatar