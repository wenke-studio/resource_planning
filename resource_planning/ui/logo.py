import reflex as rx

from resource_planning.components.react_icons import tbler_icons


def logo(class_name: str = "text-3xl") -> rx.Component:
    return tbler_icons(
        tag="TbCirclePlus2",
        class_name=class_name,
    )
