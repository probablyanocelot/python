import kivy
import time
import datetime as dt
import keyboard
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.config import Config
Config.set('graphics', 'fullscreen', 'fake')


# Window.clearcolor = .3, .3, .3, 1

# Builder.load_string("""
# <MyClock>:
#     orientation: 'vertical'
#     Label:
#         id: kv_sec
#         text: root.current_time
#         font_size: '90dp'
#         text_size: self.size
#         halign: 'center'
#         valign: 'middle'
# """)


# year = now.strftime("%Y")
# print("year:", year)

# month = now.strftime("%m")
# print("month:", month)

# day = now.strftime("%d")
# print("day:", day)

# time = now.strftime("%H:%M:%S")
# print("time:", time)


# print("date and time:", date_time)


class ScreenManagement(ScreenManager):
    pass


class HomeScreen(Screen):
    pass


class TodayScreen(Screen):
    pass


class TomorrowScreen(Screen):
    pass


class HomeScreenLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(ClockLabel())


class ClockLabel(Label):
    def __init__(self, **kwargs):
        super(ClockLabel, self).__init__(**kwargs)
        Clock.schedule_interval(lambda dt: self.update_time(), 1)
        # current_time = StringProperty('')
        self.clocktimer()
        # self.text = str(current_time)

# https://kivy.org/doc/stable/api-kivy.clock.html
    def clocktimer(self):
        while True:
            self.time = dt.datetime.now()
            Clock.schedule_once(self.clocktimer, 0.5)

    def update_time(self):
        now = dt.datetime.now()  # current date and time
        date_time = now.strftime("%m/%d/%Y, %I:%M:%S %p")
        self.text = date_time  # str(dt.datetime.now())


class PiClock(Widget):
    def __init__(self, **kwargs):
        super(PiClock, self).__init__(**kwargs)

        return MyClock()


class Goalie(App):
    def __init__(self, **kwargs):
        super(Goalie, self).__init__(**kwargs)
        # Window.maximize()

        # establish previous_screen variable to be used in the back button
        self.previous_screen = ""

    def build(self):
        return ScreenManagement()


if __name__ == '__main__':
    Goalie().run()
