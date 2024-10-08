import os
from pathlib import Path
from typing import Optional

import reflex as rx

BASE_DIR = Path(__file__).parent


class ClerkComponent(rx.Component):
    library: str = "@clerk/clerk-react"


class ClerkState(rx.State):
    is_signed_in: bool = False

    user_id: str = ""

    claims: str = ""

    user: str = ""

    def set_clerk_session(self, token: str):
        self.is_signed_in = True
        # todo: decode the jwt token than set user_id and claims
        self.user_id = 1

        # todo: trigger .fetch_user()
        if self.user_id:
            self.fetch_user()

    def clear_clerk_session(self):
        self.is_signed_in = False
        # todo: needs to dosomething
        pass

    def fetch_user(self):
        # todo: create clerk api than fill me
        self.user = "test"
        # if self.user_id:
        #     self.user = clerk.api.get_user(self.user_id)
        #     self.set_user(self.user)


class ClerkSessionHandler(rx.Component):
    tag: str = "ClerkSessionHandler"

    def add_imports(self) -> dict:
        return {
            "@clerk/clerk-react": ["useAuth"],
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
