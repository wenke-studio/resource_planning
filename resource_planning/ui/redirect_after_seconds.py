import asyncio
from typing import AsyncIterable, Callable

import reflex as rx


class RedirectAfterSeconds(rx.ComponentState):
    async def waiting(
        self, to: str, seconds: int
    ) -> AsyncIterable[rx.event.EventSpec | None]:
        while True:
            await asyncio.sleep(1)
            if seconds <= 0:
                break
            seconds -= 1
            yield
        yield rx.redirect(to)

    @classmethod
    def get_component(
        cls,
        seconds: int,
        to: str,
        as_: Callable[[], rx.Component],
    ) -> rx.Component:
        return as_(on_mount=lambda: cls.waiting(to, seconds))


def redirect_after_seconds(
    seconds: int = 5,
    to: str = "/",
    as_: Callable[[], rx.Component] | None = rx.spinner,
) -> rx.Component:
    return RedirectAfterSeconds.create(
        seconds=seconds,
        to=to,
        as_=as_,
    )
