from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder

from libs.screens.home_page import Homepage

class InstagramApp(MDApp):
    def build(self):
        Window.size = [300, 600]
        self.load_all_kv_files()
        return Homepage()


    def load_all_kv_files(self):
        Builder.load_file('libs/screens/home_page.kv')
        Builder.load_file('libs/screens/appbar.kv')
        Builder.load_file('libs/screens/story_creator.kv')
        Builder.load_file('libs/screens/bottom_nav.kv')
        Builder.load_file('libs/screens/circular_avatar_image.kv')
        Builder.load_file('libs/screens/post_card.kv')


    def on_start(self):
        self.root.dispatch('on_enter')


if __name__ == '__main__':
    InstagramApp().run