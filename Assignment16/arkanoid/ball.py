import random
import arcade

class Ball(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.center_x = game.width // 2
        self.center_y = 60
        self.change_x = random.choice([-1, 1])
        self.change_y = random.choice([-1, 1])
        self.radius = 15
        self.speed = 4
        self.width = self.radius * 2 
        self.height = self.radius * 2
        self.color = arcade.color.WHITE

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)

    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed
