from typing import Callable

import reflex as rx

from resource_planning.components import clerk, react_icons

default_meta = [
    {
        "name": "viewport",
        "content": "width=device-width, shrink-to-fit=no, initial-scale=1",
    },
]


def header(title: str):
    return rx.flex(
        rx.hstack(
            react_icons.tbler_icons("TbHeartRateMonitor", class_name="text-3xl"),
            rx.heading(title),
        ),
        rx.box(
            clerk.signed_in(
                rx.hstack(
                    clerk.user_button(),
                    clerk.sign_out_button(rx.button("Sign Out")),
                )
            ),
            clerk.signed_out(clerk.sign_in_button(rx.button("Sign In"))),
        ),
        align_items="center",
        justify_content="space-between",
        class_name="h-16 p-8",
    )


def sidebar():
    return rx.vstack(
        rx.link("Home", href="/"),
        rx.link("public", href="/public"),
        rx.link("private", href="/private"),
        class_name="border border-red-500 w-52",
    )


def page_loading() -> rx.Component:
    return rx.center(
        rx.spinner(size="3"),
        class_name="w-full h-screen justify-center items-center",
    )


def page(
    route: str,
    title: str | None = None,
    description: str | None = None,
    meta: list[dict[str, str]] | None = None,
    on_load: rx.event.EventHandler | list[rx.event.EventHandler] | None = None,
) -> Callable[[Callable[[], rx.Component]], rx.Component]:
    def decorator(page_content: Callable[[], rx.Component]) -> rx.Component:
        def template_page() -> rx.Component:
            return clerk.clerk_provider(
                clerk.clerk_loading(page_loading()),
                clerk.clerk_loaded(
                    header(title="title"),
                    sidebar(),
                    page_content(),
                ),
            )

        all_meta = [*default_meta]
        if meta:
            all_meta.extend(meta)

        @rx.page(
            route=route,
            title=title,
            description=description,
            meta=all_meta,
            on_load=on_load,
        )
        def wrapper() -> rx.Component:
            return template_page()

        return wrapper

    return decorator
