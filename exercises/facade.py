# Provides a simple, easy to understand/user interface
# over a large and sophisticated blocks of code.

from random import randint

class Generator:
    def generate(self, count):
        return [randint(1,9) for x in range(count)]

class Splitter:
    def split(self, array):
        result = []

        row_count = len(array)
        col_count = len(array[0])

        for r in range(row_count):
          the_row = []
          for c in range(col_count):
            the_row.append(array[r][c])
          result.append(the_row)

        for c in range(col_count):
          the_col = []
          for r in range(row_count):
            the_col.append(array[r][c])
          result.append(the_col)

        diag1 = []
        diag2 = []

        for c in range(col_count):
          for r in range(row_count):
            if c == r:
              diag1.append(array[r][c])
            r2 = row_count - r - 1
            if c == r2:
              diag2.append(array[r][c])

        result.append(diag1)
        result.append(diag2)

        return result

class Verifier:
    def verify(self, arrays):
        first = sum(arrays[0])

        for i in range(1, len(arrays)):
          if sum(arrays[i]) != first:
            return False

        return True

class MagicSquareGenerator:
    def generate(self, size):
        generator = Generator()
        splitter = Splitter()
        verifier = Verifier()

        while True:
            list_of_nums = generator.generate(size * size)
            square = []
            for row in range(0, len(list_of_nums), size):
                square.append(list_of_nums[row:row + size])
            # square = [list_of_nums[i:i + size] for i in range(0, len(list_of_nums), size)]
            split = splitter.split(square)
            if verifier.verify(split):
                return square


if __name__ == '__main__':
    magic_square = MagicSquareGenerator().generate(3)
    for row in magic_square:
        print(row)
