class Points:
    def __init__(self):
        # Initializes points
        self.points = 0
        
    def add_points(self, add):
        # Adds points if true/ if hit gem otherwise 
        # subtract for hitting rock.
        if add:
            self.points += 75
        else:
            self.points -= 50