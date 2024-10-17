import reflex as rx


class Spline(rx.Component):
    scene: rx.Var[str]

    library = "@splinetool/react-spline"
    lib_dependencies: list[str] = ["@splinetool/runtime@1.5.5"]
    tag = "Spline"
    is_default = True


def spline(scene: str, **props: dict) -> rx.Component:
    return Spline.create(scene=scene, **props)
