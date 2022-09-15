import kivy
import time
import datetime as dt
import keyboard
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window
from KivyOnTop import register_topmost, unregister_topmost

from kivy.config import Config
Config.set('graphics', 'fullscreen', 'fake')


# Window.clearcolor = .3, .3, .3, 1

Builder.load_string("""
<MyClock>:
    orientation: 'vertical'
    Label:
        id: kv_sec
        text: root.current_time
        font_size: '90dp'
        text_size: self.size
        halign: 'center'
        valign: 'middle'
""")


# year = now.strftime("%Y")
# print("year:", year)

# month = now.strftime("%m")
# print("month:", month)

# day = now.strftime("%d")
# print("day:", day)

# time = now.strftime("%H:%M:%S")
# print("time:", time)


# print("date and time:", date_time)

TITLE = 'MyClock'


class MyClock(BoxLayout):
    current_time = StringProperty('')

# https://kivy.org/doc/stable/api-kivy.clock.html
    def clocktimer(self):
        while True:
            self.time = dt.now()
            Clock.schedule_once(self.clocktimer, 0.5)


class PiClock(App):

    def build(self, *args):
        Clock.schedule_interval(lambda dt: self.update_time(), 1)
        return MyClock()

    def update_time(self):
        now = dt.datetime.now()  # current date and time
        date_time = now.strftime("%m/%d/%Y, %I:%M:%S %p")
        self.root.current_time = date_time  # str(dt.datetime.now())

    def on_start(self, *args):
        Window.set_title(TITLE)
        register_topmost(Window, TITLE)
        Window.borderless = True
        Window.maximize()
        self.show = True
        keyboard.add_hotkey(r'shift + alt + space',
                            lambda: self.hide_show(self.show))

    def hide_show(self, show):
        if show:
            self.show = False
            return Window.hide()
        else:
            self.show = True
            return Window.restore()


if __name__ == '__main__':
    PiClock().run()
