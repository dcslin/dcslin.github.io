from nicegui import ui
class Example:
    def __init__(self) -> None:
        @ui.page("/example1")
        def page():
            ui.link("home","/")
            ui.label("example1")

            