# using toga as the GUI framework
import os

import toga
from toga.style.pack import *


class MyDetailedList(toga.App):

    def startup(self):
        self.main_window = toga.MainWindow(title=self.name)

        self.box = toga.Box('box1')
        data1 = ['Item 0', 'Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5', 'Item 6', 'Item 7']
        self.detailedlist = toga.DetailedList(data=data1, on_select=self.selection_handler, style=Pack(flex=1))

        self.box.add(self.detailedlist)

        self.main_window.content = self.box
        self.main_window.show()

    def selection_handler(widget, selection):
        print('Row {} of widget {} was selected.'.format(selection, widget))


def main():
    return MyDetailedList('MyDetailedList', 'org.pybee.detailedlist')


if __name__ == '__main__':
    main().main_loop()
