from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image

Window.size = (800, 600)

class MainScreen(Screen):
    def go_to_game_selection(self, *args):
        self.manager.current = 'game_selection'

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.add_widget(layout)

        self.titel = Label(text='Гра', font_size='48sp', size_hint=(1, 0.8))
        layout.add_widget(self.titel)

        play_button = Button(text='Грати', size_hint=(1, 0.2))
        play_button.bind(on_press=self.go_to_game_selection)
        layout.add_widget(play_button)


class  GameSelectionScreen(Screen):
    def go_to_game_basketbal(self, *args):
        self.manager.current = 'basketball'

    def go_to_game_football(self, *args):
        self.manager.current = 'football'

    def __init__(self, **kwargs):
        super( GameSelectionScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.add_widget(layout)

        play_button = Button(text='баксетбол', size_hint=(1, 0.2))
        play_button.bind(on_press=self.go_to_game_basketbal)
        layout.add_widget(play_button)

        play_button = Button(text='футбол', size_hint=(1, 0.2))
        play_button.bind(on_press=self.go_to_game_football)
        layout.add_widget(play_button)

class Football(Screen):
    def __init__(self, **kwargs):
        super(Football).__init__(**kwargs)
        layout = FloatLayout()
        self.add_widget(layout)

        self.background = Image(socure = 'football.png', size_hint=(1,1))
        layout.add_widget(self.background)

        self.ball = Image(sourse = "football ball.png",)


class ClikerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(GameSelectionScreen(name='game_selection'))
        return sm

if __name__ == '__main__':
    ClikerApp().run()



