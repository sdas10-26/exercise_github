class Car:
    """
    A class that represents the drive and direction of a car.

    Attributes:
        x(int): Represents the x-coordiante of the car's position.
        y(int): Represents the y-coordinate of the car's position.
        heading(str): Direction that the car is facing ie.('n', 'e', 's', or 'w').

    Methods:
        turn(direction): Changes the car's heading depending on the direction ie.('l' for left and 'r' for right).
        drive(distance: int = 1): Moves the car in the direction that it is currently moving in.
        status(): Prints the coordinates and the heading of the specified car.
    """
    def __init__(self):
        """
        Initializes the car starting at coordinates (0,0) and facing "n" for north
        """
        self.x = 0
        self.y = 0 
        self.heading = "n" #(n for north)
    def turn(self, direction):
        """
        Turns the car left('l') or right('r') based on its heading. 
        """
        if self.heading == "n":
            self.heading = "w" if direction == "l" else "e"
        elif self.heading == "e":
            self.heading = "n" if direction == "l" else "s"
        elif self.heading == "s":
            self.heading = "e" if direction == "l" else "w"
        elif self.heading =="w":
            self.heading = "s" if direction == "l" else "n"
    def drive(self, distance: int = 1):
        """
        Car moves forward by the distance in he cars current heading.
        """
        if self.heading == "n":
            self.heading += distance
        elif self.heading == "w":
            self.heading += distance
        elif self.heading == "e":
            self.heading += distance
        elif self.heading == "s":
            self.heading += distance
    def status(self):
        """
        Prints the car's coordinates and heading.
        """
        print(f"Coordinates : ({self.x}, {self.y})")
        print(f"Heading: {self.heading}")
        