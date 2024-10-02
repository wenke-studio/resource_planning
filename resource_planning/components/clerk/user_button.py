from .base import Clerk


class UserButton(Clerk):
    """UserButton component of Clerk

    A prebuilt component that comes styled out of the box to show the avatar
    from the account the user is signed in with.
    """

    tag = "UserButton"


user_button = UserButton.create
