from kivy.app import App
from kivy.lang import Builder

from kivy.uix.gridlayout import GridLayout

Builder.load_file('widget/home/home.kv')


class Home(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def take_test(self):
        App.get_running_app().root.current = "test_step_1"
