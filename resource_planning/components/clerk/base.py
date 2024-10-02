import reflex as rx

import os


class ClerkComponent(rx.Component):
    library: str = "@clerk/clerk-react"


class ClerkProvider(ClerkComponent):
    tag: str = "ClerkProvider"

    publishable_key: str = os.getenv("CLERK_PUBLISHABLE_KEY")


clerk_provider = ClerkProvider.create
