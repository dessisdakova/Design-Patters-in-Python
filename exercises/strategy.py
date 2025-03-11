# Enables the exact behaviour of a system to be selected at run-time.

import cmath
import math
from abc import ABC


class DiscriminantStrategy(ABC):
    """
    Strategy Pattern: Defines a strategy for calculating the discriminant.
    Allows different algorithms to be used interchangeably.
    """
    def calculate_discriminant(self, a, b, c):
        """Calculates the discriminant of a quadratic equation."""
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    """
    Concrete Strategy: Calculates the discriminant without restrictions.
    """
    def calculate_discriminant(self, a, b, c):
        return b**2 - 4*a*c


class RealDiscriminantStrategy(DiscriminantStrategy):
    """
    Concrete Strategy: Calculates the discriminant only for real roots.
    Returns NaN if the discriminant is negative.
    """
    def calculate_discriminant(self, a, b, c):
        result = b**2 - 4*a*c
        if result < 0:
            return float('nan')
        return result


class QuadraticEquationSolver:
    """
    Context: Uses a strategy to solve a quadratic equation.
    Allows the strategy to be changed at runtime.
    """
    def __init__(self, strategy):
        """Initializes the solver with a discriminant strategy."""
        self.strategy = strategy

    def solve(self, a, b, c):
        """
        Solves the quadratic equation ax^2 + bx + c = 0.
        Returns a pair of complex values.
        """
        discriminant = complex(self.strategy.calculate_discriminant(a, b, c), 0)
        root_disc = cmath.sqrt(discriminant)
        x1 = (-b + root_disc) / (2 * a)
        x2 = (-b - root_disc) / (2 * a)
        return (x1, x2)


if __name__ == '__main__':
    solver1 = QuadraticEquationSolver(OrdinaryDiscriminantStrategy())
    result1 = solver1.solve(1, 4, 1)
    print(f"Ordinary Strategy: {result1}")

    solver2 = QuadraticEquationSolver(RealDiscriminantStrategy())
    result2 = solver2.solve(1, 4, 5)
    print(f"Real Strategy: {result2}")
