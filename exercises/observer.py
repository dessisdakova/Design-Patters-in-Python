# Observer is the object that wished to be informed
# about events happening in the system.
# The entity generating events is observable.

class Game:
    """
    Observer Pattern: Observable (Subject) that notifies observers (rats) of changes.
    Maintains a list of rats and notifies them when a rat enters or leaves.
    """
    def __init__(self):
        """Initializes the game with an empty list of rats."""
        self.rats = []

    def rat_enters(self, rat):
        """Adds a rat to the game and notifies all rats."""
        self.rats.append(rat)
        self.notify_rats()

    def rat_leaves(self, rat):
        """Removes a rat from the game and notifies all rats."""
        self.rats.remove(rat)
        self.notify_rats()

    def notify_rats(self):
        """Notifies all rats about the current number of rats in the game."""
        for rat in self.rats:
            rat.attack = len(self.rats)


class Rat:
    """
    Observer Pattern: Observer that gets notified of changes in the game.
    Updates its attack based on the number of rats in the game.
    """
    def __init__(self, game):
        """Initializes the rat and registers it with the game."""
        self.game = game
        self.attack = 1
        self.game.rat_enters(self)

    def __enter__(self):
        """Allows using the Rat object in a with statement."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Removes the rat from the game when exiting the with statement."""
        self.game.rat_leaves(self)


if __name__ == '__main__':
    game = Game()

    r1 = Rat(game)
    print("First rat enters game.")
    print(f"Rat 1 attack: {r1.attack}") # Output: Rat 1 attack: 1
    r2 = Rat(game)
    print("Second rat enters game.")
    print(f"Rat 1 attack: {r1.attack}") # Output: Rat 1 attack: 2
    print(f"Rat 2 attack: {r1.attack}") # Output: Rat 2 attack: 2
    print("Third rat enters game.")
    with Rat(game) as r3:
        print(f"Rat 1 attack: {r1.attack}") # Output: Rat 1 attack: 3
        print(f"Rat 2 attack: {r1.attack}") # Output: Rat 2 attack: 3
        print(f"Rat 3 attack: {r1.attack}") # Output: Rat 3 attack: 3
    print("Third rat leaves game.")
    print(f"Rat 1 attack: {r1.attack}") # Output: Rat 1 attack: 2
    print(f"Rat 2 attack: {r1.attack}") # Output: Rat 2 attack: 2
