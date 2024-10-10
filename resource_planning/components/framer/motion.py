import reflex as rx

# from typing import


class Motion(rx.Component):
    library = "framer-motion"

    tag = "motion.div"

    initial: rx.Var[dict[str, float | str]]

    animate: rx.Var[dict[str, float | str]]

    exit: rx.Var[dict[str, float | str]]

    transition: rx.Var[dict[str, float | str]]

    variants: rx.Var[dict[str, dict[str, float | str]]]

    while_hover: rx.Var[dict[str, dict[str, float | str]]]

    while_tap: rx.Var[dict[str, dict[str, float | str]]]

    while_in_view: rx.Var[dict[str, dict[str, float | str]]]


motion = Motion.create
