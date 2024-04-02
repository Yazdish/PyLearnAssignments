import random
import arcade

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Better Move Sprite with Keyboard Example"

MOVEMENT_SPEED = 5


class Player(arcade.Sprite):

    def update(self):
        """ Move the player """
        # Move player.
        # Remove these lines if physics engine is moving player.
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Check for out-of-bounds
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

class Enemy(arcade.Sprite):
    def __init__(self, width, height):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.center_x = random.randint(0, width)
        self.center_y = height + 24
        self.angle = 180
        self.width = 50
        self.height = 50
        self.speed = 4


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """
        Initializer
        """

        # Call the parent class initializer
        super().__init__(width, height, title)

        # Variables that will hold sprite lists
        self.player_list = None

        # Set up the player info
        self.player_sprite = None
        self.me = Player

        # Track the current state of what key is pressed

        self.left_pressed = False

        self.right_pressed = False

        self.up_pressed = False

        self.down_pressed = False


        # Set the background color
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = Player(":resources:images/space_shooter/playerShip2_orange.png", SPRITE_SCALING)
        self.player_sprite.center_x = SCREEN_WIDTH // 2
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)
        self.them = Enemy(self.width, self.height)

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen
        self.clear()

        # Draw all the sprites.
        self.player_list.draw()

        arcade.draw_lrwh_rectangle_textured(0 ,0 ,self.width ,self.height , self.background)
        self.me.draw()
        self.them.draw()


    def update_player_speed(self):



        # Calculate speed based on the keys pressed

        self.player_sprite.change_x = 0

        self.player_sprite.change_y = 0



        if self.up_pressed and not self.down_pressed:

            self.player_sprite.change_y = MOVEMENT_SPEED

        elif self.down_pressed and not self.up_pressed:

            self.player_sprite.change_y = -MOVEMENT_SPEED

        if self.left_pressed and not self.right_pressed:

            self.player_sprite.change_x = -MOVEMENT_SPEED

        elif self.right_pressed and not self.left_pressed:

            self.player_sprite.change_x = MOVEMENT_SPEED


    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update to move the sprite
        # If using a physics engine, call update player to rely on physics engine
        # for movement, and call physics engine here.
        self.player_list.update()
        self.them.center_y -= self.them.speed

    def on_key_press(self, key, modifiers):

        """Called whenever a key is pressed. """



        if key == arcade.key.UP:

            self.up_pressed = True

            self.update_player_speed()

        elif key == arcade.key.DOWN:

            self.down_pressed = True

            self.update_player_speed()

        elif key == arcade.key.LEFT:

            self.left_pressed = True

            self.update_player_speed()

        elif key == arcade.key.RIGHT:

            self.right_pressed = True

            self.update_player_speed()



    def on_key_release(self, key, modifiers):

        """Called when the user releases a key. """



        if key == arcade.key.UP:

            self.up_pressed = False

            self.update_player_speed()

        elif key == arcade.key.DOWN:

            self.down_pressed = False

            self.update_player_speed()

        elif key == arcade.key.LEFT:

            self.left_pressed = False

            self.update_player_speed()

        elif key == arcade.key.RIGHT:

            self.right_pressed = False

            self.update_player_speed()



def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()