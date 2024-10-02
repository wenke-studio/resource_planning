from .base import ClerkComponent


class SignIn(ClerkComponent):
    tag: str = "SignIn"


class SignUp(ClerkComponent):
    tag: str = "SignUp"


class GoogleOneTap(ClerkComponent):
    tag: str = "GoogleOneTap"


sign_in = SignIn.create
sign_up = SignUp.create
google_one_tap = GoogleOneTap.create
