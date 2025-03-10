# A partially or fully initialized object
# that you clone (copy) and make use of it.

import copy


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end

    def deep_copy(self):
        st = copy.deepcopy(self.start)
        en = copy.deepcopy(self.end)
        return Line(st, en)


if __name__ == '__main__':
    start = Point(1,5)
    end = Point(5, 7)
    line1 = Line(start, end)
    line2 = line1.deep_copy()

    print(line1 == line2)
    print(line1 is line2)