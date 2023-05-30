from kivy.app import App
from kivy.lang import Builder

from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen

from widget.results.results import Results

Builder.load_file('widget/test/testStep.kv')


class Step(GridLayout):
    def __init__(self, index, total, answers, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.index = index
        self.ids.test_image.source = f"imgs/test_pt_{index}.jpg"
        self.answers = answers
        self.total = total
        self.screen_manager = screen_manager

    def previous(self, *args):
        if self.index >= 2:
            App.get_running_app().root.current = f"test_step_{self.index - 1}"
        else:
            App.get_running_app().root.current = "home"

    def next(self, *args):
        answer = int(self.ids.input.text)
        try:

            self.answers[self.index - 1] = answer
        except:
            self.answers.append(answer)

        if self.total <= self.index:
            results = list(map(int, self.answers))
            results_screen = Screen(name="testResult")
            results_screen.add_widget(
                Results(results=results, screen_manager=self.screen_manager, instance=results_screen))
            self.screen_manager.add_widget(results_screen)
            App.get_running_app().root.current = "testResult"
        else:
            App.get_running_app().root.current = f"test_step_{self.index + 1}"

    def is_int(str):
        try:
            int(str)
            return True
        finally:
            return False
