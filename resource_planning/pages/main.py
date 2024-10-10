import time

import reflex as rx

from resource_planning.components import clerk, react_icons
from resource_planning.layout import page


class MainState(rx.State):
    def on_load(self):
        print("main state on_load")

    @rx.var
    def last_touch_time(self) -> str:
        # This is updated anytime the state is updated.
        return time.strftime("%H:%M:%S")


@page(
    route="/",
    title="main page",
    description="main desc.",
    meta=[{"name": "hello", "content": "world"}],
    on_load=MainState.on_load,
)
def index():
    return rx.box(
        rx.hstack(
            rx.box(
                rx.text("content"),
                rx.text(clerk.ClerkState.user.id, class_name="text-sky-500"),
                rx.text(clerk.ClerkState.user.name, class_name="text-green-500"),
                rx.text(clerk.ClerkState.token, class_name="text-red-500"),
                rx.text(clerk.ClerkState.user, class_name="border border-sky-500"),
            ),
        ),
    )


@page(route="/public")
def public_view():
    return rx.box(
        rx.hstack(
            rx.box(
                rx.text("content"),
            ),
        ),
    )


def protected_page(func):
    def wrapper(*args, **kwargs):
        return rx.fragment(
            clerk.signed_in(
                func(*args, **kwargs),
            ),
            clerk.signed_out(
                clerk.redirect_to_sign_in(),
            ),
        )

    return wrapper


@page(route="/private")
@protected_page
def private_view():
    return rx.box(
        rx.hstack(
            rx.box(
                rx.text("content"),
            ),
        ),
    )
