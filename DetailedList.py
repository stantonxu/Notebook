# using toga as the GUI framework
import os

import toga
from toga.style.pack import *


class MyDetailedList(toga.App):

    def startup(self):
        self.main_window = toga.MainWindow(title=self.name)

        self.box = toga.Box('box1')
        self.detailedlist = toga.DetailedList('list1', style=Pack(flex=1))

        self.box.add(self.detailedlist)

        self.main_window.content = self.box
        self.main_window.show()


def main():
    return MyDetailedList('MyDetailedList', 'org.pybee.detailedlist')


if __name__ == '__main__':
    main().main_loop()
