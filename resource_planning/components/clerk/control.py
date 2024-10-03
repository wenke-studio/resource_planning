from .base import ClerkComponent


class AuthenticationWithRedirectionCallback(ClerkComponent):
    tag: str = "AuthenticationWithRedirectionCallback"


class ClerkLoaded(ClerkComponent):
    tag: str = "ClerkLoaded"


class ClerkLoading(ClerkComponent):
    tag: str = "ClerkLoading"


class Protect(ClerkComponent):
    tag: str = "Protect"


class MultisessionAppSupport(ClerkComponent):
    tag: str = "MultisessionAppSupport"


class RedirectToSignIn(ClerkComponent):
    tag: str = "RedirectToSignIn"


class RedirectToSignUp(ClerkComponent):
    tag: str = "RedirectToSignUp"


class RedirectToUserProfile(ClerkComponent):
    tag: str = "RedirectToUserProfile"


class RedirectToOrganizationProfile(ClerkComponent):
    tag: str = "RedirectToOrganizationProfile"


class RedirectToCreateOrganization(ClerkComponent):
    tag: str = "RedirectToCreateOrganization"


class SignedIn(ClerkComponent):
    tag: str = "SignedIn"


class SignedOut(ClerkComponent):
    tag: str = "SignedOut"


authentication_with_redirection_callback = AuthenticationWithRedirectionCallback.create
clerk_loaded = ClerkLoaded.create
clerk_loading = ClerkLoading.create
protect = Protect.create
multisession_app_support = MultisessionAppSupport.create
redirect_to_sign_in = RedirectToSignIn.create
redirect_to_sign_up = RedirectToSignUp.create
redirect_to_user_profile = RedirectToUserProfile.create
redirect_to_organization_profile = RedirectToOrganizationProfile.create
redirect_to_create_organization = RedirectToCreateOrganization.create
signed_in = SignedIn.create
signed_out = SignedOut.create
