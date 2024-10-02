import reflex as rx
from dotenv import load_dotenv

from .pages.main import index


load_dotenv("../.env")

app = rx.App()
app.add_page(index)
