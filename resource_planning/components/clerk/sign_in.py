from .base import Clerk


class SignIn(Clerk):
    tag = "SignIn"


class SignedIn(Clerk):
    """SignedIn Component of Clerk

    Children of this component can only be seen while signed in
    """

    tag = "SignedIn"


class SignInButton(Clerk):
    """SignInButton Component of Clerk

    An unstyled component that links to the sign-in page
    or displays the sign-in modal.
    """

    tag = "SignInButton"


sign_in = SignIn.create
signed_in = SignedIn.create
sign_in_button = SignInButton.create
