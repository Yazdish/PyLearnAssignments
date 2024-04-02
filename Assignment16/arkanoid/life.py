import arcade

class Life(arcade.Sprite):
    def __init__(self, x):
        super().__init__()
        self.center_x = x + 33
        self.center_y = 11
        self.width = 45
        self.height = 15
        self.color = arcade.color.BLACK
        self.lose_life_sound = arcade.load_sound(':resources:sounds/lose2.wav',False)
    
    def lose_life(self):
        arcade.play_sound(self.lose_life_sound)

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)