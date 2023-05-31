from kivy.app import App
from kivy.lang import Builder

from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen

from utilities.evaluateIshihara import evaluate_ishihara
from widget.camera.cameraWidget import CameraWidget

Builder.load_file('widget/results/results.kv')


class Results(GridLayout):

    def __init__(self, screen_manager, results, instance, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = screen_manager
        self.screen = instance
        self.type = evaluate_ishihara(results)

        if self.type == "deu":
            self.ids.results.text = "Se ha identificado Deuteranopia"
        elif self.type == "prot":
            self.ids.results.text = "Se ha identificado Protanopia"
        else:
            self.ids.results.text = "No se ha identificado ninguna anomalia"
            self.ids.go.text = "Tomar el test de nuevo"



    def to_home(self):
        App.get_running_app().root.current = "home"
        self.screen_manager.remove_widget(self.screen)

    def daltonice(self):
        if self.type == "deu" or self.type == "prot":
            camera = Screen(name="camera")
            camera.add_widget(CameraWidget(type=self.type, screen_manager=self.screen_manager, instance=camera))
            self.screen_manager.add_widget(camera)
            App.get_running_app().root.current = "camera"
            self.screen_manager.remove_widget(self.screen)
        else:
            App.get_running_app().root.current = "test_step_1"
            self.screen_manager.remove_widget(self.screen)
