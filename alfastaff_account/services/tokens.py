"""This module contain TokenGenerator class."""

from django.contrib.auth.tokens import PasswordResetTokenGenerator

from six import text_type


class TokenGenerator(PasswordResetTokenGenerator):
    """TokenGenerator class with function make hash value."""

    def _make_hash_value(self, user: object, timestamp: int) -> str:
        """Funtion for generate hash value."""
        return (
            text_type(user.pk) +
            text_type(timestamp) +
            text_type(user.is_active)
        )


account_activation_token = TokenGenerator()  # create TokenGenerator object
