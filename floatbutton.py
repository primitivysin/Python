from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class RootWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.add_widget(Button(text='Hello Wolrd', size_hint=(.5, .5),pos_hint={'center_x':.5, 'center_y':.5}))

class MainApp(App):

    def build(self):
        self.root = root = RootWidget()
        root.bind(size=self.update_rect, pos=self.update_rect)
        
        with root.canvas.before:
            Color(0,1,0,1)
            self.rect = Rectangle(size=root.size,pos=root.pos)
            return root
        
    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

if __name__ == '__main__':
    MainApp().run()

                          