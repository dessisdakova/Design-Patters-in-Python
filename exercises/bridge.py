# Bridges are used to decouple abstraction from implementation.
# Both can exist as hierarchies.

from abc import ABC, abstractmethod


class Renderer(ABC):
    """
    Bridge Pattern: Represents the implementation interface.
    It defines the contract for rendering shapes.
    """
    @property
    @abstractmethod
    def what_to_render_as(self):
        return None


class VectorRenderer(Renderer):
    """Bridge Pattern: Concrete implementation for vector rendering."""
    @property
    def what_to_render_as(self):
        return "lines"

class RasterRenderer(Renderer):
    """Bridge Pattern: Concrete implementation for raster rendering."""
    @property
    def what_to_render_as(self):
        return "pixels"

class Shape:
    """
    Bridge Pattern: Represents the abstraction.
    It defines the high-level shape operations, decoupled from rendering.
    """
    def __init__(self, renderer: Renderer):
        """The bridge is created when the implementation is passes as a parameter in the constructor for the abstraction."""
        self.renderer = renderer
        self.name = None

    def __str__(self):
        return f"Drawing {self.name} as {self.renderer.what_to_render_as}"

class Square(Shape):
    """Bridge Pattern: Refined abstraction for a square shape."""
    def __init__(self, renderer: Renderer):
        super().__init__(renderer)
        self.name = "Square"

class Triangle(Shape):
    """Bridge Pattern: Refined abstraction for a triangle shape."""
    def __init__(self, renderer: Renderer):
        super().__init__(renderer)
        self.name = "Triangle"


if __name__ == '__main__':
    print(Triangle(RasterRenderer())) # Triangle rendered as pixels
    print(Triangle(VectorRenderer())) # Triangle rendered as lines
    print(Square(RasterRenderer())) # Square rendered as pixels
    print(Square(VectorRenderer())) # Square rendered as lines
