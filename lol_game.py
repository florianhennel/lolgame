from keyboard import on_press
import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from matplotlib.backend_bases import button_press_handler
from matplotlib.pyplot import pink, text
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    name = ObjectProperty(None)
    last = ObjectProperty(None)

    def btn(self):
        print(f"Name: {self.name.text} {self.last.text}")
    pass

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()