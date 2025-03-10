# Bridges are used to decouple abstraction from implementation.
# Both can exist as hierarchies.

from abc import ABC, abstractmethod


class Renderer(ABC):
    """Represent the implementation."""
    @property
    @abstractmethod
    def what_to_render_as(self):
        return None


class VectorRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return "lines"

class RasterRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return "pixels"

class Shape:
    """Represent the abstraction."""
    def __init__(self, renderer: Renderer):
        """The bridge is created when the implementation is passes as a parameter in the constructor for the abstraction."""
        self.renderer = renderer
        self.name = None

    def __str__(self):
        return f"Drawing {self.name} as {self.renderer.what_to_render_as}"

class Square(Shape):
    def __init__(self, renderer: Renderer):
        super().__init__(renderer)
        self.name = "Square"

class Triangle(Shape):
    def __init__(self, renderer: Renderer):
        super().__init__(renderer)
        self.name = "Triangle"


if __name__ == '__main__':
    print(Triangle(RasterRenderer()))
    print(Triangle(VectorRenderer()))
    print(Square(RasterRenderer()))
    print(Square(VectorRenderer()))