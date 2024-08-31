from nicegui import ui
from page import Example

ui.link('example1', '/example1')

example = Example()

ui.run()