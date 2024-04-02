import random
from typing import Optional
import arcade
from arcade import Texture
from fighter import Fighter
from enemy import Enemy
from bullet import Bullet
import time

DEFAULT_FONT_SIZE = 45
    

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=600, height= 800, title= "StarWars 2023")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = Fighter(self, self.width, self.height, "YODA")
        self.them = []
        self.game_start_time = time.time()
        self.start_time = time.time()
        self.health_image = arcade.load_texture(":resources:images/backgrounds/stars.png")


    def on_draw(self):
        arcade.start_render()
        # arcade.draw_lrwh_rectangle_textured(0 ,0 ,self.width ,self.height , self.background)
        
        if self.me.health <= 0:
            arcade.draw_text('GAME OVER', self.width//2-200, self.height//2, arcade.color.ORANGE, DEFAULT_FONT_SIZE //2, width=400, align='center')
        else:
            for i in range(self.me.health):
                arcade.draw_lrwh_rectangle_textured(10+i*35 ,10 ,30 ,30 ,self.health_image, self.background)
                arcade.draw_text('Score: %i'%self.me.score, self.width-130, 10, arcade.color.RED, DEFAULT_FONT_SIZE //2, width=200, align='left')


        self.me.draw()

        for enemy in self.them:
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
            
        elif symbol == arcade.key.SPACE:
            self.me.fire()

    def on_key_release(self, symbol: int, modifiers: int):
        self.me.change_x = 0
        self.me.change_y = 0

    def on_update(self, delta_time: float):
        
        self.me.move()

        for enemy in self.them:
            if arcade.check_for_collision(self.me, enemy):
                arcade.draw_text("Game Over 💀",self.width//2-200, self.height//2, arcade.color.ORANGE, DEFAULT_FONT_SIZE //2, width=400, align='center' )
                exit(0)

        for enemy in self.them:
            enemy.move()

        for bullet in self.me.bullet_list:
            bullet.move()

        for enemy in self.them:
            for bullet in self.me.bullet_list:
                if arcade.check_for_collision(enemy, bullet):
                    self.them.remove(enemy)
                    self.me.bullet_list.remove(bullet)
                    self.me.score += 1

        for enemy in self.them:
            if enemy.center_y < 0:
                self.them.remove(enemy)

        if random.randint(1, 100) == 6:
            self.new_enemy = Enemy(self.width, self.height)
            self.them.append(self.new_enemy)


window = Game()
arcade.run()