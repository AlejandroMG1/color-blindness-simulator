from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from widget.home.home import Home
from widget.test.testStep import Step


class MyApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.answers = []

    def build(self):
        screen_manager = ScreenManager()
        home = Screen(name="home")
        home.add_widget(Home())
        screen_manager.add_widget(home)

        for i in range(18):
            screen = Screen(name=f"test_step_{i + 1}")
            screen.add_widget(Step(index=i + 1, total=18, answers=self.answers), id(f"step_{i + 1}"))
            screen_manager.add_widget(screen)

        return screen_manager


if __name__ == '__main__':
    MyApp().run()
