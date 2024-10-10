import os
from pathlib import Path
from typing import Optional

import reflex as rx

BASE_DIR = Path(__file__).parent


class ClerkComponent(rx.Component):
    library: str = "@clerk/clerk-react"


class ClerkUser(rx.Base):
    id: str = ""
    name: Optional[str] = None
    image: Optional[str] = None
    email: Optional[str] = None


class ClerkState(rx.State):
    token: Optional[str] = None
    user: Optional[ClerkUser] = None

    def set_clerk_session(self, token: str, user: dict) -> None:
        self.set_token(token)
        self.set_user(
            ClerkUser(
                id=user["id"],
                name=user["username"] or user["fullName"],
                image=user["imageUrl"],
                email=user["primaryEmailAddress"]["emailAddress"],
            )
        )

    def clear_clerk_session(self):
        self.set_token(None)
        self.set_user(None)


class ClerkSessionHandler(rx.Component):
    tag: str = "ClerkSessionHandler"

    def add_imports(self) -> dict:
        return {
            "@clerk/clerk-react": ["useAuth", "useUser"],
            "react": ["useContext", "useEffect"],
            "/utils/context": ["EventLoopContext"],
            "/utils/state": ["Event"],
        }

    def add_custom_code(self) -> list[str]:
        clerk_state_name = ClerkState.get_full_name()
        with open(BASE_DIR / "custom_code" / "clerk_session_handler.js") as f:
            custom_code = f.read() % (clerk_state_name, clerk_state_name)
        return [custom_code]


class ClerkProvider(ClerkComponent):
    tag: str = "ClerkProvider"

    publishable_key: Optional[str] = None

    secret_key: Optional[str] = None

    @classmethod
    def create(cls, *children, **props) -> rx.Component:
        props["publishable_key"] = os.getenv("CLERK_PUBLISHABLE_KEY")
        assert props["publishable_key"] is not None, "`publishable_key` is required"

        props["secret_key"] = os.getenv("CLERK_SECRET_KEY")
        assert props["secret_key"] is not None, "`secret_key` is required"

        session_handler = ClerkSessionHandler.create(*children)
        provider = super().create(session_handler, **props)
        return rx.fragment(provider)


clerk_provider = ClerkProvider.create
