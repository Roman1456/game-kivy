from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window

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
        play_button.bind(on_press=self.go_to_game_selection())
        layout.add_widget(play_button)
class ClikerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        return sm

if __name__ == '__main__':
    ClikerApp().run()



