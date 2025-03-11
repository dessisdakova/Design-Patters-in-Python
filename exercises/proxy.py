# A class that functions as an interface to a particular resource.
# That resource may be remote, expensive to construct,
# or may require logging or some other added functionality.

class Person:
    def __init__(self, age):
        self.age = age

    def drink(self):
        return 'drinking'

    def drive(self):
        return 'driving'

    def drink_and_drive(self):
        return 'driving while drunk'


class ResponsiblePerson:
    """
    Proxy Pattern: Acts as a proxy to a Person object, adding restrictions.
    Controls access to the Person's methods based on age.
    """
    def __init__(self, person):
        """Initializes the ResponsiblePerson with a Person object."""
        self.person = person

    def drink(self):
        """Allows drinking if age is 18 or older."""
        if self.person.age < 18:
            return "too young"
        else:
            return self.person.drink()

    def drive(self):
        """Allows driving if age is 16 or older."""
        if self.person.age < 16:
            return "too young"
        else:
            return self.person.drive()

    def drink_and_drive(self):
        """Always returns 'dead' regardless of age."""
        return "dead"


if __name__ == '__main__':
    rp = ResponsiblePerson(Person(25))
    print(rp.drink()) # Output: drinking
    rp.person.age = 15
    print(rp.drive()) # Output: too young
    print(rp.drink()) # Output: too young
    print(rp.drink_and_drive()) # Output: dead
