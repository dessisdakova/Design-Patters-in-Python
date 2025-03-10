# Enables the exact behaviour of a system to be selected at run-time.

import cmath
import math
from abc import ABC


class DiscriminantStrategy(ABC):
    def calculate_discriminant(self, a, b, c):
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        return b**2 - 4*a*c


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        result = b**2 - 4*a*c
        if result < 0:
            return float('nan')
        return result


class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        """ Returns a pair of complex (!) values """
        # quadratic equation: ax^2 + bx + c = 0
        discriminant = complex(self.strategy.calculate_discriminant(a, b, c), 0)
        root_disc = cmath.sqrt(discriminant)
        x1 = (-b + root_disc) / (2 * a)
        x2 = (-b - root_disc) / (2 * a)
        return (x1, x2)
