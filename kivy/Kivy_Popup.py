from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition


class CustomScreen(Screen):

    def __init__(self, **kwargs):
        super(CustomScreen, self).__init__(**kwargs)
        self.layout = AnchorLayout()

        self.popup = Popup(title='Popup', content=Label(
            text='Hello World'), size_hint=(None, None), size=(400, 400))

        self.button = Button(text=self.name, font_size=50)
        self.button.bind(on_press=self.popup.open)

        self.layout.add_widget(self.button)

        self.add_widget(self.layout)


class TestApp(App):

    def build(self):
        self.title = 'Test App'
        root = ScreenManager()

        for x in range(4):
            root.add_widget(CustomScreen(name='Screen %d' % x))

        return root


if __name__ == '__main__':
    # And run the App with its method 'run'
    TestApp().run()
