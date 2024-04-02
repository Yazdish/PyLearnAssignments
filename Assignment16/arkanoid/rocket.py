import arcade

class Rocket(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.center_x = game.width // 2
        self.center_y = 60
        self.change_x = 0
        self.change_y = 0
        self.width = 60
        self.height = 20
        self.color = arcade.color.BLACK
        self.speed = 4
        self.score = 0
        self.life = 3


    def move(self, game):
        
        self.center_x += self.change_x * self.speed

        if self.center_x < 60:
            self.center_x = 60

        if self.center_x > game.width - 60 :
            self.center_x = game.width - 60

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)