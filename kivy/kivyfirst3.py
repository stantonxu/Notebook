import kivy
kivy.require("1.10.0")

from kivy.app import App 
from kivy.uix.button import Button 

class TestApp(App):

    def build(self):
        return Button(text="hello world")

TestApp().run()