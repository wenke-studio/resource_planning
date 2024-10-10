from typing import Callable

import reflex as rx

from resource_planning.components import react_icons
from resource_planning.ui import logo


def header() -> rx.Component:
    return rx.box(
        rx.hstack(
            logo(),
            react_icons.tbler_icons(tag="TbMenu2", class_name="text-3xl"),
            class_name="justify-between p-2 h-full items-center",
        ),
        class_name="h-16 fixed top-0 inset-x-0 border-b border-white/30",
    )


def landing_page(content: rx.Component) -> Callable:
    def wrapper(*args, **kwargs) -> rx.Component:
        return rx.center(
            header(),
            rx.box(
                content(*args, **kwargs),
                class_name="w-full h-full",
            ),
            class_name="w-full min-h-screen pt-16",
        )

    return wrapper
