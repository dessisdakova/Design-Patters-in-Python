# A partially or fully initialized object
# that you clone (copy) and make use of it.

import copy


class Point:
    """Represents a point in 2D space."""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line:
    """
    Prototype Pattern: Represents a line segment.
    Provides a deep_copy method to create a copy of the line.
    """
    def __init__(self, start=Point(), end=Point()):
        """Initializes the line with start and end points."""
        self.start = start
        self.end = end

    def deep_copy(self):
        """Creates a deep copy of the line."""
        st = copy.deepcopy(self.start)
        en = copy.deepcopy(self.end)
        return Line(st, en)


if __name__ == '__main__':
    start = Point(1,5)
    end = Point(5, 7)
    line1 = Line(start, end)
    line2 = line1.deep_copy()

    print(line1 == line2) # Output: False
    print(line1 is line2) # Output: False
