from kivy.app import App
from kivy.lang import Builder

from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen

from widget.camera.cameraWidget import CameraWidget

Builder.load_file('widget/home/home.kv')


class Home(GridLayout):

    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = screen_manager

    def take_test(self):
        App.get_running_app().root.current = "test_step_1"

    def deuteranopia(self):
        camera = Screen(name="camera")
        camera.add_widget(CameraWidget(type="deu", screen_manager=self.screen_manager, instance=camera))
        self.screen_manager.add_widget(camera)
        App.get_running_app().root.current = "camera"

    def protanopia(self):
        camera = Screen(name="camera")
        camera.add_widget(CameraWidget(type="prot", screen_manager=self.screen_manager, instance=camera))
        self.screen_manager.add_widget(camera)
        App.get_running_app().root.current = "camera"
