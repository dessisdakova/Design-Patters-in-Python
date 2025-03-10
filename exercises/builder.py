# When piecewise construction ob object is complicated,
# provide an API for doing it succinctly.

class CodeBuilder:

    def __init__(self, root_name):
        self.root_name = root_name
        self.attributes = []

    def add_field(self, name, value):
        self.attributes.append((name, value))
        return self

    def __str__(self):
        attributes_as_strings = []
        for field in self.attributes:
            text = f"    self.{field[0]} = {field[1]}\n"
            attributes_as_strings.append(text)
        all_fields = "".join(attributes_as_strings)
        if self.attributes:
            return f"class {self.root_name}:\n  def __init__(self):\n{all_fields}"
        else:
            return f"class {self.root_name}:\n  pass"


if __name__ == '__main__':
    cb = CodeBuilder('Person').add_field('name', '""') \
                              .add_field('age', '0')
    print(cb)

    cb2 = CodeBuilder('Foo')
    print(cb2)