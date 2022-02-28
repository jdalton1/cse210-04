from location import Location
from movingObjects import MovingObjects
from points import Points
import random


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service, bottom_y):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._bottom_y = bottom_y
        score = Points()
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity) 


    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        gems = cast.get_actors("gems")
        rocks = cast.get_actors("rocks")

        # banner.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        robot_position = robot.get_position()

        for gem in gems:
            speed = random.randint(2, 10)
            velocity = Location(0, speed)
            gem.set_velocity(velocity)
            gem.move_next(max_x, max_y)
            gem_position = gem.get_position()

            if gem_position == robot_position:
                cast.remove_actor("gems", gem)

        for rock in rocks:
            speed = random.randint(2, 10)
            velocity = Location(0, speed)
            rock.set_velocity(velocity)
            rock.move_next(max_x, max_y)
            rock_position = rock.get_position()

            if rock_position == robot_position:

                stop_velosity = Location(0,0)
                rock.set_velocity(stop_velosity)
                rock.remove_actor("rocks", rock)
        # artifacts = MovingObjects
        
        # artifacts.Move_Objects()


        # for artifact in artifacts:
        #     if robot.get_position() == artifact.get_position():
        #         # message = artifact.get_message()
        #         # banner.set_text(message)    
        #         pass
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()