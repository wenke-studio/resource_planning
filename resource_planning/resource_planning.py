import reflex as rx
from dotenv import load_dotenv

from .pages import *  # noqa: F403

load_dotenv("../.env")

app = rx.App()
