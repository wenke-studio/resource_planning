from .base import ClerkComponent


class UserButton(ClerkComponent):
    tag: str = "UserButton"


class UserProfile(ClerkComponent):
    tag: str = "UserProfile"


user_button = UserButton.create
user_profile = UserProfile.create
