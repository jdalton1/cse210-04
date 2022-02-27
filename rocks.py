from player import Player
from color import Color
import random

class Rocks(Player):

    def __init__(self):
        super().__init__
        self.set_text("o")
        red = random.randint(50,255)
        green = random.randint(50,255)
        blue = random.randint(50,255)
        self.set_color(Color(red, green, blue))
        self.set_position([random.randint(8,892),0])
        self.set_velocity([0,1])