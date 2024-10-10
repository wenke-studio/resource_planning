import reflex as rx

from resource_planning.components import framer
from resource_planning.layouts.landing_page import landing_page


@rx.page(route="/", title="Studio")
@landing_page
def welcome() -> rx.Component:
    return rx.box(
        rx.center(
            rx.heading("Welcome"),
        ),
        rx.center(
            framer.motion(
                rx.center("o", class_name="w-16 h-16"),
                animate={"x": [-100, 100, 0]},
                transition={"ease": "easeOut", "duration": 2},
            ),
        ),
        class_name="",
    )
