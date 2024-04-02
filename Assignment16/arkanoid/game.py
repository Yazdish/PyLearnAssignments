from typing import Optional, Tuple
import arcade
import pyglet
from ball import Ball
from rocket import Rocket
from brick import Brick
from life import Life

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width= 600, height= 800, title="Arkanoid")
        self.background = arcade.load_texture(':resources:images/backgrounds/abstract_1.jpg')
        self.player = Rocket(self)
        self.ball = Ball(self)
        self.bricks = []
        self.life = []
        self.x = 25
        self.y = 600
        self.xleft = 0

        for _ in range(3):
            self.new_life = Life(self.xleft)
            self.xleft += 45
            self.life.append(self.new_life)

        self.color = [arcade.color.BABY_BLUE, arcade.color.BABY_BLUE_EYES, arcade.color.WHITE, arcade.color.PINK, arcade.color.AMERICAN_ROSE]
        
        for i in range(5):
            for _ in range(11):
                self.brick = Brick(self.x, self.y, self.color[i])
                self.bricks.append(self.brick)
                self.x += 55                
            self.y += 35
            self.x = 25

    def on_draw(self):
        arcade.start_render()

        if self.life:
            for block in self.bricks:
                block.draw()
            
            self.player.draw()
            self.ball.draw()
            for life in self.life:
                life.draw()
            arcade.draw_text(f'SCORE: {self.player.score}', 5, 780, arcade.color.AMERICAN_ROSE, 15, 2,'left',('calibri', 'calibri'), True)
        arcade.finish_render()

    def on_update(self):
        if self.life:
            self.ball.move()
            self.player.move()
            
            if self.ball.center_x < 2 or self.ball.center_x > self.width-2:
                self.ball.change_x *= -1

            if self.ball.center_y > self.height:
                self.ball.change_y *= -1
            
            if arcade.check_for_collision(self.player, self.ball):
                self.ball.change_y *= -1

            for count, block in enumerate(self.bricks):
                if arcade.check_for_collision(self.ball, block):
                    self.ball.change_y *= -1
                    self.ball.speed += 0.2
                    self.player.score += 1
                    self.player.speed += 0.1
                    del self.bricks[count]

            if self.ball.center_y < 0:
                del self.ball
                self.new_life.lose_life()
                self.life.pop()
                self.ball = Ball(self)
            if not self.life:
                self.game_over()
    

    def on_key_press(self, symbol: int, modifiers: int):

        if symbol == arcade.key.LEFT or symbol == arcade.key.A :
            self.player.change_x = -1
        elif symbol == arcade.key.RIGHT or symbol == arcade.key.D:
            self.player.change_x = 1
        elif symbol == arcade.key.DOWN:
            self.player.change_x = 0

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        
        if self.player.width-75 < x < self.width-self.player.width+75:
            self.player.center_x = x

    def game_over(self):
        self.bricks = []
        self.life = []
        del self.ball
        del self.player
        arcade.set_background_color(arcade.color.WHITE)
        self.background = arcade.draw_text("GAME OVER!", self.width // 2, self.height // 2, arcade.color.BLACK_LEATHER_JACKET, font_size= 45)

if __name__ == '__main__':
     game = Game()
     arcade.run()