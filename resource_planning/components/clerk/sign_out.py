from .base import Clerk


class SignedOut(Clerk):
    """SignedOut Component of Clerk

    Children of this component can only be seen while signed out
    """

    tag = "SignedOut"


signed_out = SignedOut.create
