import reflex as rx
from reflex.utils.imports import ImportVar


class ReactIcons(rx.Component):
    library: str
    lib_dependencies: list[str] = ["react-icons"]

    @classmethod
    def create(cls, tag: str, **props) -> rx.Component:
        component = super().create(**props)
        component.tag = tag
        return component

    @property
    def import_var(self):
        return ImportVar(
            tag=self.tag,
            is_default=self.is_default,
            alias=self.alias,
            transpile=self._should_transpile(self.library),
            # ! avoid to install the `.library`
            install=False,
        )
