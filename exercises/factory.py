# A component responsible solely for the wholesome
# (not piecewise) creation of objects.

class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"Person with ID {self.id} is {self.name}"


class PersonFactory:
    def __init__(self):
        self.index = 0  # Instance-level index

    def create_person(self, name):
        person = Person(self.index, name)
        self.index += 1
        return person


if __name__ == '__main__':
    pf = PersonFactory()
    print(pf.create_person("John"))
    print(pf.create_person("Kate"))