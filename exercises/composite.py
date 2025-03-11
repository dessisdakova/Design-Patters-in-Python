# Composite lets you treat individual objects and compositions of objects uniformly.
# Creates a tree-like structure where individual objects (leaves)
# and composite objects (branches) have a common interface.

from abc import ABC, abstractmethod
from collections.abc import Iterable


class Summable(ABC, Iterable):
    """
    Composite Pattern: Component interface.
    Defines the common interface for both individual objects and composites.
    """
    @property
    @abstractmethod
    def sum(self):
        """Calculates the sum of the object."""
        pass

class SingleValue(Summable):
    """
    Composite Pattern: Leaf node.
    Represents an individual object with a single value.
    """
    @property
    def sum(self):
        """Returns the value itself as the sum."""
        return self.value

    def __init__(self, value):
        """Initializes the SingleValue with a value."""
        self.value = value

    def __iter__(self):
        """Make a single object iterable."""
        yield self

class ManyValues(list, Summable):
    """
    Composite Pattern: Composite node.
    Represents a collection of Summable objects.
    """
    def append(self, item):
        """Adds a Summable object to the collection."""
        if not isinstance(item, Summable):
            item = SingleValue(item)
        super().append(item)

    @property
    def sum(self):
        """Calculates the sum of all objects in the collection."""
        total = 0
        for x in self:
            total += x.sum
        return total


if __name__ == '__main__':
    single_value = SingleValue(11)
    other_values = ManyValues()
    other_values.append(22)
    other_values.append(33)
    # make a list of all values
    all_values = ManyValues()
    all_values.append(single_value)
    all_values.append(other_values)
    print(all_values.sum) # Output: 66
