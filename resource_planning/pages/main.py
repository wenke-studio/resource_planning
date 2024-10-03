import reflex as rx

from resource_planning.components import clerk, react_icons


def providers(func):
    def wrapper(*args, **kwargs):
        return clerk.clerk_provider(
            clerk.clerk_session(
                clerk.clerk_loading(
                    rx.center(
                        rx.spinner(size="3"),
                        class_name="w-full h-screen justify-center items-center",
                    )
                ),
                clerk.clerk_loaded(
                    func(*args, **kwargs),
                ),
            )
        )

    return wrapper


def sidebar():
    return rx.vstack(
        rx.link("Home", href="/"),
        rx.link("public", href="/public"),
        rx.link("private", href="/private"),
        class_name="border border-red-500 w-52",
    )


def header(title: str):
    return rx.flex(
        rx.hstack(
            react_icons.tbler_icons("TbHeartRateMonitor", class_name="text-3xl"),
            rx.heading(title),
        ),
        rx.box(
            clerk.signed_in(clerk.user_button()),
            clerk.signed_out(clerk.sign_in_button(rx.button("Sign In"))),
        ),
        align_items="center",
        justify_content="space-between",
        class_name="h-16 p-8",
    )


def content(*children, **props):
    return rx.box(
        *children,
        rx.box(
            clerk.signed_in(
                clerk.sign_out_button(
                    # todo: debug only
                    rx.button("Sign Out", variant="ghost"),
                ),
            ),
            class_name="fixed bottom-8 right-8",
        ),
        class_name="border border-blue-500 w-full",
        **props,
    )


@rx.page(route="/")
@providers
def index():
    return rx.box(
        header("Resource Planning"),
        rx.hstack(
            sidebar(),
            content(
                rx.text("content"),
            ),
        ),
    )


@rx.page(route="/public")
@providers
def public_view():
    return rx.box(
        header("Public View"),
        rx.hstack(
            sidebar(),
            content(
                rx.text("content"),
            ),
        ),
    )


@rx.page(route="/private")
@providers
def private_view():
    return rx.box(
        header("Private View"),
        rx.hstack(
            sidebar(),
            content(
                rx.text("content"),
            ),
        ),
    )
