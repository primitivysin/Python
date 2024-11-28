from kivy.app import App
from kivy.base import Clock
from kivy.uix.widget import Widget

class PongGame(Widget):
    pass

class PongApp(App):
    def build(self):
        return PongGame()
    
class PongGame(Widget):
    def update(self, dt):
        pass

class PongApp(App):
    def update(self):
        game = PongGame()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game

class PongGame(Widget):

    def update(self,dt):
        self.ball.move()
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_x *= -1
        if (self.ball.x<0) or (self.ball.right> self.width):
            self.ball.velocity_x *= -1
        
if __name__ == '__main__':
    PongApp().run()
