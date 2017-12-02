from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class Grid(GridLayout):
    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Hello World'))
        self.add_widget(Button(text='Close App'))
        

class TestApp(App):
    def build(self):
        return Grid()


TestApp().run()