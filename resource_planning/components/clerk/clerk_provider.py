import reflex as rx
from .base import Clerk


class ClerkProvider(Clerk):
    tag: str = "ClerkProvider"

    # todo: fill this key
    publishable_key: rx.Var[str] = ""


clerk_provider = ClerkProvider.create
