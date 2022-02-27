import os
import random
from re import L
from player import Player

# from player import Player
from rocks import Rocks
from gems import Gems
from movingObjects import MovingObjects
from cast import Cast

from director import Director

from keyboard import KeyboardService
from display import VideoService

from color import Color
from location import Location



FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 40

def main():
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    
    
    # create the cast
    moving_objects = MovingObjects(keyboard_service, MAX_X, MAX_Y)
    cast = moving_objects.cast
    
    # create the banner
    banner = Player()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Location(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot
    x = int(MAX_X / 2)
    bottom_y = int(MAX_Y / 8)
    y = int(MAX_Y - bottom_y)
    position = Location(x, y)

    robot = moving_objects._player
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    # create the artifacts
    falling_objects = ["gems", "rocks"]
   
    
    for n in range(DEFAULT_ARTIFACTS):
        x = random.randint(1, COLS - 1)
        y = 1
        position = Location(x, y)
        position = position.scale(CELL_SIZE)

        falling_object = random.choice(falling_objects)
        if falling_object == "gems":
            velocity = Location(0, 10)
            artifact = Gems(position, velocity)
            symbol = "*"
            text = "gems"



        else:
            velocity = Location(0, 1)
            artifact = Rocks(position, velocity)
            symbol = "o"
            text = "rocks"
        



        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        

        artifact.set_text(symbol)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        artifact.set_velocity(velocity)
        # artifact.set_message(message)
        cast.add_actor(text, artifact)    
    
    # start the game
    
    terminate_y = MAX_Y - bottom_y
    director = Director(keyboard_service, video_service, terminate_y)
    director.start_game(cast)


if __name__ == "__main__":
    main()