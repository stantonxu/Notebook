# using toga as the GUI framework
import os

import toga
from toga.style.pack import *


class Notebook(toga.App):
    # def action_saveas(self, widget):
    #     self.main_window.save_file_dialog('Save as...', 'notebook1.txt')

    def startup(self):
        self.main_window = toga.MainWindow(title=self.name)

        # box = toga.Box(
        #     children=[
        #         toga.MultilineTextInput(id='input1')
        #     ], 
        #     style=Pack(direction=COLUMN)
        # )

        self.box = toga.Box('box1')
        self.textinput = toga.MultilineTextInput('input1', style=Pack(flex=1))

        # load file here
        with open('notebook1.txt') as f:
            self.textinput.value = f.read()
        f.close()

        self.box.add(self.textinput)

        # cmd_savaas = toga.Command(
        #     # action=self.action_saveas,
        #     action=self.save_file,
        #     label='Save as...',
        #     tooltip='Save to local file'
        # )

        self.main_window.content = self.box
        # self.main_window.toolbar.add(cmd_savaas)
        self.main_window.show()

    def save_file(self):
        # notebook1.txt = textinput.value
        f = open('notebook1.txt', 'w')
        f.write(self.textinput.value)
        f.close()

    def exit(self):
        self.save_file()
        super().exit()


def main():
    return Notebook('Notebook', 'org.pybee.notebook')


if __name__ == '__main__':
    main().main_loop()
