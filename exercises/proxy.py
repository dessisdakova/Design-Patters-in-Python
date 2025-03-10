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
    def __init__(self, person):
        self.person = person

    def drink(self):
        if self.person.age < 18:
            return "too young"
        else:
            return self.person.drink()

    def drive(self):
        if self.person.age < 16:
            return "too young"
        else:
            return self.person.drive()

    def drink_and_drive(self):
        return "dead"


if __name__ == '__main__':
    rp = ResponsiblePerson(Person(25))
    print(rp.drink())
    rp.person.age = 15
    print(rp.drive())
    print(rp.drink())
    print(rp.drink_and_drive())