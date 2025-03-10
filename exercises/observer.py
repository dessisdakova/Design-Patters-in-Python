# # Observer is the object that wished to be informed
# about events happening in the system.
# The entity generating events is observable.

class Game:
    def __init__(self):
        self.rats = []

    def rat_enters(self, rat):
        self.rats.append(rat)
        self.notify_rats()

    def rat_leaves(self, rat):
        self.rats.remove(rat)
        self.notify_rats()

    def notify_rats(self):
        for rat in self.rats:
            rat.attack = len(self.rats)


class Rat:
    def __init__(self, game):
        self.game = game
        self.attack = 1
        self.game.rat_enters(self)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.game.rat_leaves(self)


if __name__ == '__main__':
    game = Game()

    r1 = Rat(game)
    print("First rat enters game.")
    print(f"Rat 1 attack: {r1.attack}")
    r2 = Rat(game)
    print("Second rat enters game.")
    print(f"Rat 1 attack: {r1.attack}")
    print(f"Rat 2 attack: {r1.attack}")
    print("Third rat enters game.")
    with Rat(game) as r3:
        print(f"Rat 1 attack: {r1.attack}")
        print(f"Rat 2 attack: {r1.attack}")
        print(f"Rat 3 attack: {r1.attack}")
    print("Third rat leaves game.")
    print(f"Rat 1 attack: {r1.attack}")
    print(f"Rat 2 attack: {r1.attack}")