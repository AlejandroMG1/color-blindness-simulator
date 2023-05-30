import cv2
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout

from utilities.img_procesing import daltonice

Builder.load_file('widget/camera/cameraWidget.kv')


class CameraWidget(GridLayout):

    def __init__(self, screen_manager, type, instance, **kwargs):
        super().__init__(**kwargs)
        self.type = type
        self.capture = cv2.VideoCapture(0)
        self.screen = instance
        self.schedule = Clock.schedule_interval(self.update, 1.0 / 33.0)
        self.screen_manager = screen_manager

    def update(self, dt):
        ret, frame = self.capture.read()
        # convert it to texture
        buf1 = cv2.flip(frame, 0)
        buf1 = daltonice(buf1, self.type)
        buf = buf1.tostring()
        texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        # if working on RASPBERRY PI, use colorfmt='rgba' here instead, but stick with "bgr" in blit_buffer.
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        # display image from the texture
        self.ids.cam.texture = texture1

    def back(self):
        Clock.unschedule(self.schedule)
        self.capture.release()
        App.get_running_app().root.current = "home"
        self.screen_manager.remove_widget(self.screen)

