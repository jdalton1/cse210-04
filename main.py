import os
import random
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


def main():
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    
    # create the cast
    moving_objects = MovingObjects(keyboard_service, MAX_X, MAX_Y)
    cast = moving_objects.cast
    
    # create the banner
    # banner = Actor()
    # banner.set_text("")
    # banner.set_font_size(FONT_SIZE)
    # banner.set_color(WHITE)
    # banner.set_position(Location(CELL_SIZE, 0))
    # cast.add_actor("banners", banner)
    
    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y / 2)
    position = Location(x, y)

    robot = cast._player
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    # create the artifacts
    # with open(DATA_PATH) as file:
    #     data = file.read()
    #     messages = data.splitlines()
    falling_objects = ["gems", "rocks"]
    # artifacts = []
    
    for n in range(DEFAULT_ARTIFACTS):
        falling_object = random.choice(falling_objects)
        # artifacts.append(falling_object)
           
        text = chr(random.randint(33, 126))
        # message = messages[n]

        x = random.randint(1, COLS - 1)
        y = 1
        position = Location(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        # artifact = MovingObjects()
        # artifact.set_text(text)
        # artifact.set_font_size(FONT_SIZE)
        # artifact.set_color(color)
        # artifact.set_position(position)
        # artifact.set_message(message)
        cast.add_actor("artifacts", falling_object)    
    
    # start the game

    director.start_game(cast)


if __name__ == "__main__":
    main()