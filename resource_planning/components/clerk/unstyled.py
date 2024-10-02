from .base import ClerkComponent


class SignInButton(ClerkComponent):
    tag: str = "SignInButton"


class SignInWithMetamaskButton(ClerkComponent):
    tag: str = "SignInWithMetamaskButton"


class SignUpButton(ClerkComponent):
    tag: str = "SignUpButton"


class SignOutButton(ClerkComponent):
    tag: str = "SignOutButton"


sign_in_button = SignInButton.create
sign_in_with_metamask_button = SignInWithMetamaskButton.create
sign_up_button = SignUpButton.create
sign_out_button = SignOutButton.create
