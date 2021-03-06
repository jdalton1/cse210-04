from cast import Cast
from location import Location
from player import Player
"""
This class needs to control movment for every object in the game"""

class MovingObjects:
    def __init__(self, keyboard, max_x, max_y):
        """
        No Arguments.
        Set up variables that don't need to be modified.
        Reterns nothing."""
        self._player_velocity = 2
        self.cast = Cast()
        self._keyboard_service = keyboard
        self._player = Player()
        self._max_x = max_x
        self._max_y = max_y

    
    def Move_Objects(self):
        """
        Argument: max_y, get the position equal to the bottom of the screen.
        Uses the lists in cast to move objects down.
        Returns nothing."""
        """
        gem_list = cast.get_actors("gem")   #Get actors by group so code in line 29 can work properly. This is for the gem group
        for gem in gem_list: #loop through the list of classes and move them down accoridng to thier velocity
            velocity = gem.Get_Velocity() #Allows objects to have diffrent velocity just like the example shown by the teacher
            position = gem.Get_Position() #Get the position of the cast member
            position[1] = position[1] + velocity[1] #Calculate new y position
            if position [1] > max_y:   #We need to make sure objects below the screen are removed
                cast.remove_actor("gem", gem) #This is why I will need to get actors by groups as a group is required here
            else:   #Only move the object if it exists or it may cause an error
                cast.Set_Position(position) #Set the new position
        
        rock_list = cast.get_actors("rock")  #Same thing for the rock group
        for rock in rock_list: 
            velocity = rock.Get_Velocity() 
            position = rock.Get_Position() 
            position[1] = position[1] + velocity[1] 
            if position [1] > max_y:  
                cast.remove_actor("rock", rock) 
            else:
                cast.Set_Position(position) 
        """
        # gem_list = self.cast.get_actors("gems")
        # for gem in gem_list:
        #     gem._velocity = Location(0, 2)
        #     gem.move_next(self, self._max_x, self._max_y)
        #     gem_location = gem.get_position()
        #     if gem_location > self._max_y:
        #         self.cast.remove_actor("gem", gem)
        
        # rock_list = self.cast.get_actors("rocks")
        # for rock in rock_list:
        #     rock._velocity = Location(0, 2)
        #     rock.move_next(self, self._max_x, self._max_y)
        #     rock_location = rock.get_position()
        #     if rock_location > self._max_y:
        #         self.cast.remove_actor("rocks", rock)
    
    # def move_rocks(self):
    #     rock_list = self.cast.get_actors("rocks")
    #     for rock in rock_list:
    #         rock._velocity = Location(0, 2)
    #         rock.move_next(self, self._max_x, self._max_y)
    #         rock_location = rock.get_position()
    #         if rock_location > self._max_y:
    #             self.cast.remove_actor("rocks", rock)
    
    # def move_gems(self):
    #     gem_list = self.cast.get_actors("gems")
    #     for gem in gem_list:
    #         gem._velocity = Location(0, 2)
    #         gem.move_next(self, self._max_x, self._max_y)
    #         gem_location = gem.get_position()
    #         if gem_location > self._max_y:
    #             self.cast.remove_actor("gems", gem)
                
        
    # def Move_Player(self):
    #     """
    #     No Argument
    #     Sets the player volocity based on keyboard action/
    #     Reterns nothing"""
    #     velocity = self._keyboard_service.get_direction() #I found it would be just easier for the player object to move itself and just modify the velocity here
    #     self._player.set_velocity(velocity) 
    #     self._player.move_next(self, self._max_x, self._max_y)
        

"""
Fix up 23, 29-30. We need to go through lists by groups, looping through 1 big list will cause errors for cast.remove_actor argument 1
Waiting on gems.py and rocks.py"""