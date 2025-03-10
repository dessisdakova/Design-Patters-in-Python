# A pattern in which the object's behaviour is determent my its state.
# An object transitions from one state to another
# (something needs to trigger a transition)
# A formalized construct which manages states and transitions is called state machine.
from itertools import combinations


class CombinationLock:
    def __init__(self, combination: list):
        self.status = "LOCKED"
        self.combination = combination
        self._entered_digits = []

    def reset(self):
        self.status = "LOCKED"
        self._entered_digits = []

    def enter_digit(self, digit):
        if self.status == 'LOCKED' or self.status == 'ERROR':
            self._entered_digits = []

        self._entered_digits.append(digit)
        self.status = ''.join(map(str, self._entered_digits))

        if len(self._entered_digits) == len(self.combination):
            if self._entered_digits == self.combination:
                self.status = 'OPEN'
            else:
                self.status = 'ERROR'


if __name__ == '__main__':
    cl = CombinationLock([1, 5, 2, 4, 5])
    print("Combination: ", cl.combination)
    print("cl status after initialization: ", cl.status)
    cl.enter_digit(1)
    print("cl status after first digit: ", cl.status)
    cl.enter_digit(5)
    print("cl status after second digit: ", cl.status)
    cl.enter_digit(2)
    print("cl status after third digit: ", cl.status)
    cl.enter_digit(4)
    print("cl status after forth digit: ", cl.status)
    cl.enter_digit(5)
    print("cl status after fifth digit: ", cl.status)
