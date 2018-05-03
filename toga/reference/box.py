import toga


box = toga.Box('box1')


def button_handler(widget):
    print("button handler")


button = toga.Button('Hello world', on_press=button_handler)
box.add(button)


def build(app):
    return box


toga.App('First App', 'org.pybee.helloworld', startup=build).main_loop()
