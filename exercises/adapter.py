# A construct which adapts an existing interface X
# to conform to the required interface Y

class Square:
    def __init__(self, side=0):
        self.side = side

def calculate_area(rc):
    return rc.width * rc.height

class SquareToRectangleAdapter:
    def __init__(self, square):
        self.square = square

    @property
    def width(self):
        return self.square.side

    @property
    def height(self):
        return self.square.side


if __name__ == '__main__':
    sq = Square(5)
    print(calculate_area(SquareToRectangleAdapter(sq)))
    sq.side = 10
    print(calculate_area(SquareToRectangleAdapter(sq)))
    sq.side = 11
    print(calculate_area(SquareToRectangleAdapter(sq)))
