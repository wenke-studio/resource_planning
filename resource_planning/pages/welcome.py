import reflex as rx

from resource_planning.components import clerk
from resource_planning.layouts.landing_page import landing_page
from resource_planning.ui import redirect_after_seconds


@rx.page(route="/", title="Studio")
@landing_page
def welcome() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                rx.heading(
                    "Resource Planning",
                    class_name="w-full text-center",
                ),
                rx.text(
                    "The workspace to manage your resources.",
                    class_name="w-full text-center",
                ),
            ),
        ),
        rx.center(
            clerk.signed_out(
                clerk.sign_in(),
            ),
            clerk.signed_in(
                redirect_after_seconds(
                    seconds=3,
                    to="/dashboard",
                ),
            ),
        ),
    )


@rx.page(route="/dashboard")
def dashboard() -> rx.Component:
    return rx.box(
        rx.text("Dashboard"),
        rx.button("Back", on_click=rx.redirect("/")),
    )
