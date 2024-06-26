from typing import Optional
import arcade
from arcade import Texture


class Bullet(arcade.Sprite):
    def __init__(self, host):
        super().__init__(":resources:images/space_shooter/laserRed01.png")
        self.center_x = host.center_x
        self.center_y = host.center_y
        self.speed = 3        
        self.change_x = 0
        self.change_y = 1
        self.change_angle = 90

    def move(self):
        self.center_y += self.speed

    def collision(self):
        arcade.play_sound(arcade.sound.Sound(':resources:sounds/laser4.wav'), 0.2, 0.0,False)

