import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from matplotlib.backend_bases import button_press_handler
from matplotlib.pyplot import pink, text
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen



class MainWindow(Screen):
    pass
class Classic_game(Screen):
    pass
class Ability_game(Screen):
    pass
class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")

class MyApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MyApp().run()