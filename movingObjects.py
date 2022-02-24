from cast import Cast
from player import Player
"""
This class needs to control movment for every object in the game"""

class MovingObjects:
    def __init__(self, keyboard):
        """
        No external parameters.
        Set up variables that don't need to be modified.
        Reterns nothing."""
        _player_velocity = 2
        cast = Cast()
        _keyboard_service = keyboard
        _player = Player()

    
    def Move_Objects(self, cast):
        """
        No external parameters.
        Uses the lists in cast to move objects down.
        Returns nothing."""
        cast_list = cast.get_all_actors()   #Get actors by group so code in line 27 can work properly
        for object in cast_list:
            #loop through the list of classes and move them down accoridng to thier velocity
            velocity = object.Get_Velocity() #Allows objects to have diffrent velocity just like the example shown by the teacher
            position = object.Get_Position() #Get the position of the cast member
            position[1] = position[1] + velocity[1] #Calculate new y position
            #if position [1] > max_y:   #We need to make sure objects below the screen are removed
            #    cast.remove_actor(group, object) #This is why I will need to get actors by groups as a group is required here
            cast.Set_Position(position) #Set the new position
        
        
    def Move_Player(self):
        velocity = self._keyboard_service.get_direction() #I found it would be just easier for the player object to move itself and just modify the velocity here
        self._player.set_velocity(velocity) 
        

"""
Fix up 23, 29-30. We need to go through lists by groups, looping through 1 big list will cause errors for cast.remove_actor argument 1
Work on getting all the info from the point class of rfk"""