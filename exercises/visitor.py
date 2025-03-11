# A component (visitor) that knows how to traverse
# a data structure composed of types.

# taken from https://tavianator.com/the-visitor-pattern-in-python/

def _qualname(obj):
    """Get the fully-qualified name of an object (including module)."""
    return obj.__module__ + '.' + obj.__qualname__


def _declaring_class(obj):
    """Get the name of the class that declared an object."""
    name = _qualname(obj)
    return name[:name.rfind('.')]


# Stores the actual visitor methods
_methods = {}


# Delegating visitor implementation
def _visitor_impl(self, arg):
    """Actual visitor method implementation."""
    key = (_qualname(type(self)), type(arg))
    if not key in _methods:
        raise Exception('Key % not found' % key)
    method = _methods[key]
    return method(self, arg)


# The actual @visitor decorator
def visitor(arg_type):
    """Decorator that creates a visitor method."""

    def decorator(fn):
        declaring_class = _declaring_class(fn)
        _methods[(declaring_class, arg_type)] = fn

        # Replace all decorated methods with _visitor_impl
        return _visitor_impl

    return decorator

# ↑↑↑ LIBRARY CODE ↑↑↑

class Value:
    """Represents a numeric value in an expression."""
    def __init__(self, value):
        self.value = value


class AdditionExpression:
    """Represents an addition operation in an expression."""
    def __init__(self, left, right):
        self.right = right
        self.left = left


class MultiplicationExpression:
    """Represents a multiplication operation in an expression."""
    def __init__(self, left, right):
        self.right = right
        self.left = left


class ExpressionPrinter:
    """
    Visitor Pattern: Traverses an expression tree and prints it.
    Implements the visitor interface for different expression types.
    """
    def __init__(self):
        self.buffer = []

    @visitor(Value)
    def visit(self, v):
        """Visits a Value node and appends its value to the buffer."""
        self.buffer.append(str(v.value))

    @visitor(AdditionExpression)
    def visit(self, ae):
        """Visits an AdditionExpression node, adds parentheses, and recursively visits children."""
        self.buffer.append('(')
        self.visit(ae.left)
        self.buffer.append('+')
        self.visit(ae.right)
        self.buffer.append(')')

    @visitor(MultiplicationExpression)
    def visit(self, me):
        """Visits a MultiplicationExpression node and recursively visits children."""
        self.visit(me.left)
        self.buffer.append('*')
        self.visit(me.right)

    def __str__(self):
        """Returns the printed expression as a string."""
        return ''.join(self.buffer)


if __name__ == '__main__':
    simple = AdditionExpression(Value(2), Value(3))
    ep = ExpressionPrinter()
    ep.visit(simple)
    print(ep) # Output: (2+3)

    comp = MultiplicationExpression(AdditionExpression(Value(2), Value(3)),Value(4))
    ep2 = ExpressionPrinter()
    ep2.visit(comp)
    print(ep2) # Output: (2+3)*4
