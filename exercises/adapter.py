# A construct which adapts an existing interface X
# to conform to the required interface Y

class Square:
    def __init__(self, side=0):
        self.side = side

def calculate_area(rc):
    return rc.width * rc.height

class SquareToRectangleAdapter:
    """
    Adapter Pattern: Adapts the Square class to the interface expected by calculate_area.
    It makes a Square object look like a Rectangle object.
    """
    def __init__(self, square):
        self.square = square

    @property
    def width(self):
        """Adapts the square's side to the width property of a rectangle."""
        return self.square.side

    @property
    def height(self):
        """Adapts the square's side to the height property of a rectangle."""
        return self.square.side


if __name__ == '__main__':
    sq = Square(5)
    print(calculate_area(SquareToRectangleAdapter(sq))) # Uses the adapter to calculate area of a square
    sq.side = 10
    print(calculate_area(SquareToRectangleAdapter(sq))) # Uses the adapter again with updated square
    sq.side = 11
    print(calculate_area(SquareToRectangleAdapter(sq))) # Uses the adapter again with updated square
