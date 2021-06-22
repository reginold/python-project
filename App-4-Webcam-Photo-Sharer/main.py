from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
import wikipedia
import requests
from filesharer import FileSharer
import time
from kivy.core.clipboard import Clipboard
import webbrowser

Builder.load_file("frontend.kv")


# class FirstScreen(Screen):
#     def get_image_link(self):
#         user_query = self.manager.current_screen.ids.user_query.text
#         page = wikipedia.page(user_query)
#         page_link = page.images[0]
#         return page_link

#     def download_image(self):
#         req = requests.get(self.get_image_link())
#         image_path = 'files/image.jpg'
#         with open(image_path, 'wb') as file:
#             file.write(req.content)
#         return image_path

#     def set_image(self):
#         self.manager.current_screen.ids.img.source = self.download_image()
#         print("Working...")
class CameraScreen(Screen):
    def start(self):
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start Camera"
        self.ids.camera.texture = None
    def capture(self):
        current_file = time.strftime('%Y%m%d-%H:%M:%S')
        self.file_path = f"files/{current_file}.png"
        self.ids.camera.export_to_png(self.file_path)
        self.manager.current = "image_screen"
        self.manager.current_screen.ids.img.source = self.file_path
        

class ImageScreen(Screen):
    link_message = "Create the link first"

    def create_link(self):
        file_path = App.get_running_app().root.ids.camera_screen.file_path
        file_share = FileSharer(filepath=file_path)
        self.url = file_share.share()
        self.ids.link.text = self.url

    def copy_link(self):
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link.text = self.link_message

    def open_link(self):
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text = self.link_message 

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
