# A component that processes structures text data.
# Does so by turning it into separate lexical tokens (lexing)
# and then interpreting a sequences of said token (parsing).

import re


class ExpressionProcessor:
    def __init__(self):
        self.variables = {}

    def calculate(self, expression: str):
        # get all valid characters by one
        valid_chars = []
        operants = []
        for char in expression:
            if char in ["+", "-"]:
                valid_chars.append(char)
                operants.append(char)
            elif char.isdigit():
                valid_chars.append(char)
            elif char.isalpha() and char in self.variables.keys():
                valid_chars.append(char)
            else:
                return 0

        # resolve double-digit numbers
        values = re.split('-|\+', "".join(valid_chars))

        # check if regex matched digits with variables or any trailing operants are present
        numbers = []
        for char in values:
            if char.isdigit():
                numbers.append((int(char)))
            elif char in self.variables.keys():
                numbers.append(self.variables[char])
            else:
                return 0

        if numbers:
            result = numbers[0]
            for i in range(1, len(numbers)):
                if operants[i-1] == "+":
                    result += numbers[i]
                else:
                    result -= numbers[i]
            return result


if __name__ == '__main__':
    ep = ExpressionProcessor()
    ep.variables["a"] = 2
    print(ep.calculate("13+1-9a"))
    print(ep.calculate("13+1-a"))
    print(ep.calculate("1+1-a+"))
    print(ep.calculate("13+1-x"))
