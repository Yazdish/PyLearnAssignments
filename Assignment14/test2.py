import random
import time
from typing import Optional
import arcade
from arcade import Texture
from fighter import Fighter
from enemy import Enemy
from bullet import Bullet
    
DEFAULT_FONT_SIZE = 45

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width = 600, height = 800, title = "StarWars 2023")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = Fighter(self, self.width, self.height, "YODA")
        self.enemy_list = []
        self.game_start_time = time.time()
        self.start_time = time.time()
        # self.health_image = arcade.load_texture("")

    def on_draw(self):
        arcade.start_render()

        if self.me.health <= 0:
            arcade.draw_text("Game Over ☠", self.width // 2 - 200 , self.height // 2, arcade.color.RED_DEVIL, DEFAULT_FONT_SIZE // 2 , width= 400 , align= 'center')

        else:

            arcade.draw_lrwh_rectangle_textured(0 ,0 ,self.width ,self.height , self.background)
        
            self.me.draw()
            for i in self.me.health:
                arcade.draw_circle_filled()

            for enemy in self.enemy_list:
                enemy.draw()
            

            for bullet in self.me.bullet_list:
                bullet.draw()

        arcade.finish_render()

    def on_key_press(self, symbol, modifiers: int):
        
        if symbol == arcade.key.LEFT or symbol == arcade.key.A :
            self.me.change_x = -1

        elif symbol == arcade.key.RIGHT or symbol == arcade.key.D :
            self.me.change_x = 1
            
        elif symbol == arcade.key.W or symbol == arcade.key.UP :
            self.me.change_y = 1
            
        elif symbol == arcade.key.S or symbol == arcade.key.DOWN :
            self.me.change_y = -1
            
        elif symbol == arcade.key.Q:
            self.me.fire()

    def on_key_release(self, symbol: int, modifiers: int):
        self.me.change_x = 0
        self.me.change_y = 0

    def on_update(self, delta_time: float):
        
        self.me.move()

        for enemy in self.enemy_list:
            if arcade.check_for_collision(self.me, enemy):
                arcade.draw_text("Game Over ☠", self.width // 2 , self.height // 2, arcade.color.RED_DEVIL, DEFAULT_FONT_SIZE // 2, width= 200, align="center")
                exit(0)

        for enemy in self.enemy_list:
            enemy.move()

        for bullet in self.me.bullet_list:
            bullet.move()

        for enemy in self.enemy_list:
            for bullet in self.me.bullet_list:
                if arcade.check_for_collision(enemy, bullet):
                    self.enemy_list.remove(enemy)
                    self.me.bullet_list.remove(bullet)

        for enemy in self.enemy_list:
            if enemy.center_y < 0:
                self.enemy_list.rmove(enemy)
                self.me.health -= 1 

        if random.randint(1, 100) == 6:
            self.new_enemy = Enemy(self.width, self.height)
            self.enemy_list.append(self.new_enemy)


window = Game()
arcade.run()