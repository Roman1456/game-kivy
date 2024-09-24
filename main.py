from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen ,FadeTransition
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.animation import Animation

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
        super(GameSelectionScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.add_widget(layout)

        basketball = Button(text='баксетбол', size_hint=(1, 0.2))
        basketball.bind(on_press=self.go_to_game_basketbal)
        layout.add_widget(basketball)

        football = Button(text='футбол', size_hint=(1, 0.2))
        football.bind(on_press=self.go_to_game_football)
        layout.add_widget(football)





class Football(Screen):
    score = NumericProperty(0)
    def __init__(self, **kwargs):
        super(Football, self).__init__(**kwargs)
        layout = FloatLayout()
        self.add_widget(layout)

        self.background = Image(socure='football.png', allo_stretch=True, keep_ration=False,  size_hint=(1,1))
        layout.add_widget(self.background)

        self.ball = Image(sourse = "football ball.png", allow_stretch=True , size=(100,100))
        self.ball.pos_hint= {'center_x': 0.5, 'center_y': 0.5}
        self.ball.bind(on_touch_down= self.ball_cliked)
        layout.add_widget(self.ball)

        self.score_label = Label(text='Score: 0',font_size='24sp', size_hint=(1, 0.1))
        layout.add_widget(self.score_label)

        self.back_button = Button(text='Назад',size_hint=(1, 0.2))
        self.back_button.bind(on_press=self.go_back)
        layout.add_widget(self.back_button)

    def ball_cliked(self, instance,touch):
        if instance.collide_point(*touch.pos):
            self.score += 1
            self.score_label.text = f'Score: {self.score}'
            self.ball_cliick_animation()

    def ball_cliick_animation(self):
        anim=Animation(size=(150,150), opacity=0.5, duration = 0.2) + Animation(size=(100,100))
        anim.start(self.ball)


    def go_back(self, *args):
        self.manager.current = 'game_selection'




class ClikerApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition)
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(GameSelectionScreen(name='game_selection'))
        sm.add_widget(Football(name='football'))
        
        return sm

if __name__ == '__main__':
    ClikerApp().run()



