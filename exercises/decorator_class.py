# Facilitates the addition of behaviors to individual objects without inheriting from them.

class Circle:
  def __init__(self, radius):
    self.radius = radius

  def resize(self, factor):
    self.radius *= factor

  def __str__(self):
    return f"A circle of radius {self.radius}"


class Square:
  def __init__(self, side):
    self.side = side

  def __str__(self):
    return f"A square with side {self.side}"


class ColoredShape:
  """
  Decorator Pattern: Adds color functionality to a shape object.
  Wraps a shape and adds a color attribute.
  """
  def __init__(self, shape, color):
    """Initializes the ColoredShape with a shape and color."""
    self.color = color
    self.shape = shape

  def resize(self, factor):
    """Resizes the shape if it's a Circle."""
    if isinstance(self.shape, Circle):
        self.shape.resize(factor)

  def __str__(self):
    """Returns a string representation of the colored shape."""
    return f"{self.shape} has the color {self.color}"


if __name__ == '__main__':
  circle = ColoredShape(Circle(5), 'red')
  print(circle) # Output: A circle of radius 5 has the color red
  circle.resize(2)
  print(circle) # Output: A circle of radius 10 has the color red

  square = ColoredShape(Square(4), 'purple')
  print(square) # Output: A square with side 4 has the color purple
  square.resize(5)
  print(square) # Output: A square with side 4 has the color purple
