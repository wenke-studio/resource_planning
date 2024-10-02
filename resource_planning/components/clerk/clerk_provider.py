import reflex as rx
from .base import Clerk

import os


class ClerkProvider(Clerk):
    tag: str = "ClerkProvider"

    publishable_key: rx.Var[str] = os.getenv("CLERK_PUBLISHABLE_KEY")


clerk_provider = ClerkProvider.create
