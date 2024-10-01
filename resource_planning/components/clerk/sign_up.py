from .base import Clerk


class SignUp(Clerk):
    tag = "SignUp"


sign_up = SignUp.create
