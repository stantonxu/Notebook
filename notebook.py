# using toga as the GUI framework
import os

import toga
from toga.style.pack import *


class Notebook(toga.App):

    def startup(self):
        self.main_window = toga.MainWindow(title=self.name)

        self.box = toga.Box('box1')
        self.textinput = toga.MultilineTextInput('input1', style=Pack(flex=1))

        # load file here
        with open(os.path.dirname(__file__)+'\\notebook1.txt', 'r') as f:
            self.textinput.value = f.read()

        self.box.add(self.textinput)

        self.main_window.content = self.box
        self.main_window.show()

    def save_file(self):
        # notebook1.txt = textinput.value
        f = open(os.path.dirname(__file__)+'\\notebook1.txt', 'w')
        f.write(self.textinput.value)
        f.close()

    def exit(self):
        self.save_file()
        super().exit()


def main():
    return Notebook('Notebook', 'org.pybee.notebook')


if __name__ == '__main__':
    main().main_loop()
