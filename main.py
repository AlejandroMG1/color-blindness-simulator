import cv2
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics.texture import Texture

from widget.camera.cameraWidget import CameraWidget
from widget.home.home import Home
from widget.test.testStep import Step


class MyApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.answers = []

    def build(self):
        screen_manager = ScreenManager()
        home = Screen(name="home")
        home.add_widget(Home(screen_manager))
        screen_manager.add_widget(home)

        for i in range(20):
            screen = Screen(name=f"test_step_{i + 1}")
            screen.add_widget(Step(index=i + 1, total=20, answers=self.answers, screen_manager=screen_manager),
                              id(f"step_{i + 1}"))
            screen_manager.add_widget(screen)
        return screen_manager


if __name__ == '__main__':
    MyApp().run()
    cv2.destroyAllWindows()

# __author__ = 'bunkus'
# from kivy.app import App
# from kivy.uix.widget import Widget
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.image import Image
# from kivy.clock import Clock
# from kivy.graphics.texture import Texture
#
# import cv2
#
# class CamApp(App):
#
#     def build(self):
#         self.img1=Image()
#         layout = BoxLayout()
#         layout.add_widget(self.img1)
#         #opencv2 stuffs
#         self.capture = cv2.VideoCapture(0)
#         Clock.schedule_interval(self.update, 1.0/33.0)
#         return layout
#
#     def update(self, dt):
#         # display image from cam in opencv window
#         ret, frame = self.capture.read()
#         # convert it to texture
#         buf1 = cv2.flip(frame, 0)
#         buf = buf1.tostring()
#         texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
#         #if working on RASPBERRY PI, use colorfmt='rgba' here instead, but stick with "bgr" in blit_buffer.
#         texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
#         # display image from the texture
#         self.img1.texture = texture1
#
# if __name__ == '__main__':
#     CamApp().run()
#     cv2.destroyAllWindows()
