from player import Player
from color import Color

import random

class Gems(Player):

    def __init__(self):
        super().__init__
        self.set_text("*")
        red = random.randint(50,255)
        green = random.randint(50,255)
        blue = random.randint(50,255)
        # self._position = position
        # self._velocity = velocity
        self.set_color(Color(red, green, blue))
        # self.set_position(self._position)
        # self.set_velocity(self._velocity)



       

