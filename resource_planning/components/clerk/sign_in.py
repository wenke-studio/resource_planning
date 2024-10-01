from .base import Clerk


class SignIn(Clerk):
    tag = "SignIn"


sign_in = SignIn.create
