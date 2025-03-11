# When piecewise construction ob object is complicated,
# provide an API for doing it succinctly.

class CodeBuilder:
    """
    Builder Pattern: Constructs complex objects step by step.
    Provides a fluent interface for building class definitions.
    """
    def __init__(self, root_name):
        """Initializes the CodeBuilder with the root class name."""
        self.root_name = root_name
        self.attributes = []

    def add_field(self, name, value):
        """Adds a field (attribute) to the class definition."""
        self.attributes.append((name, value))
        return self # Returns self for method chaining (fluent interface)

    def __str__(self):
        """Generates the class definition as a string."""
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
    print(cb) # Prints the generated class definition for Person

    cb2 = CodeBuilder('Foo')
    print(cb2) # Prints the generated class definition for Foo (empty class)
