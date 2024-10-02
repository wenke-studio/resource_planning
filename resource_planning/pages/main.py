from rxconfig import config

import reflex as rx

from resource_planning.components.clerk import signed_in, user_button
from resource_planning.components.clerk import (
    clerk_provider,
    signed_out,
    sign_in_button,
)


class State(rx.State):
    """The app state."""

    ...


def main() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


def index() -> rx.Component:
    return rx.box(
        clerk_provider(
            signed_out(
                sign_in_button(),
            ),
            signed_in(
                user_button(),
            ),
        )
    )
