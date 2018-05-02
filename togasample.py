import toga

def button_handler(widget):
    print("hello")

def build(app):
    box = toga.Box()

    button = toga.Button('Hello World', on_press=button_handler)
    button.style.padding = 50
    button.style.flex = 1
    box.add(button)

    return box

def main():
    return toga.App('First App', 'org.pybee.heloworld', startup=build)

if __name__ == '__main__':
    main().main_loop()