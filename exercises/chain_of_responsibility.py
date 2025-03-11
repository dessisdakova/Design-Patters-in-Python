# A chain of components who all get the change to process a command or a query,
# optionally having a default processing implementation,
# and an ability to terminate the processing chain

class Creature:
    """
    Chain of Responsibility Pattern: Base class for creatures in the game.
    Provides default implementations for attack and defense.
    """
    def __init__(self, game, attack, defence):
        self.game = game
        self._attack = attack
        self._defense = defence

    @property
    def attack(self):
        """Returns the base attack value."""
        return self._attack

    @property
    def defense(self):
        """Returns the base defense value."""
        return self._defense

    def __str__(self):
        return f"{self.__class__.__name__} ({self.attack}/{self.defense})"

class Goblin(Creature):
    """
    Chain of Responsibility Pattern: Concrete handler for Goblin creatures.
    Modifies attack and defense based on the presence of other creatures.
    """
    def __init__(self, game, attack=1, defense=1):
        super().__init__(game, attack, defense)

    @property
    def attack(self):
        """Calculates attack based on the presence of GoblinKings."""
        attack = super().attack
        for c in self.game.creatures:
            if isinstance(c, GoblinKing) and c is not self:
                attack += 1
        return attack

    @property
    def defense(self):
        """Calculates defense based on the total number of creatures."""
        defense = super().defense
        defense = len(self.game.creatures)
        return defense


class GoblinKing(Goblin):
    """
    Chain of Responsibility Pattern: Concrete handler for GoblinKing creatures.
    Inherits from Goblin and has its own base attack and defense values.
    """
    def __init__(self, game):
        super().__init__(game, attack=3, defense=3)


class Game:
    """
    Chain of Responsibility Pattern: The game object that manages the creatures.
    Acts as the client in the pattern.
    """
    def __init__(self):
        self.creatures = []


if __name__ == '__main__':
    gm = Game()
    goblin1 = Goblin(gm)
    gm.creatures.append(goblin1)
    goblin2 = Goblin(gm)
    gm.creatures.append(goblin2)
    goblin3 = Goblin(gm)
    gm.creatures.append(goblin3)
    king_goblin = GoblinKing(gm)
    gm.creatures.append(king_goblin)

    print(goblin1) # Output: Goblin (2/4)
    print(goblin2) # Output: Goblin (2/4)
    print(goblin3) # Output: Goblin (2/4)
    print(king_goblin) # Output: GoblinKing (3/4)
