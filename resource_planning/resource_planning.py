import reflex as rx
from dotenv import load_dotenv

from .models import *  # noqa: F403
from .pages import *  # noqa: F403

load_dotenv("../.env")

style = {
    ".debug": {
        "border": "3px solid red",
    }
}

app = rx.App(
    style=style,
)
