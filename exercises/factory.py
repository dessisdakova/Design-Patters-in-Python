# A component responsible solely for the wholesome
# (not piecewise) creation of objects.

class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"Person with ID {self.id} is {self.name}"


class PersonFactory:
    """
    Factory Pattern: Creates Person objects with sequential IDs.
    Encapsulates the object creation logic.
    """
    def __init__(self):
        """Initializes the factory with an index counter."""
        self.index = 0  # Instance-level index

    def create_person(self, name):
        """Creates a Person object with a unique ID."""
        person = Person(self.index, name)
        self.index += 1
        return person


if __name__ == '__main__':
    pf = PersonFactory()
    print(pf.create_person("John")) # Output: Person with ID 0 is John
    print(pf.create_person("Kate")) # Output: Person with ID 1 is Kate
