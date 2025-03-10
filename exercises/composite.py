# Composite lets you treat individual objects and compositions of objects uniformly.
# Creates a tree-like structure where individual objects (leaves)
# and composite objects (branches) have a common interface.

from abc import ABC, abstractmethod
from collections.abc import Iterable


class Summable(ABC, Iterable):
    """The interface to uniform."""
    @property
    @abstractmethod
    def sum(self):
        pass

class SingleValue(Summable):
    """The individual object."""
    @property
    def sum(self):
        return self.value

    def __init__(self, value):
        self.value = value

    def __iter__(self):
        """Make a single object iterable."""
        yield self

class ManyValues(list, Summable):
    """The composition - a box of individual objects."""
    def append(self, item):
        if not isinstance(item, Summable):
            item = SingleValue(item)
        super().append(item)

    @property
    def sum(self):
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
    print(all_values.sum)