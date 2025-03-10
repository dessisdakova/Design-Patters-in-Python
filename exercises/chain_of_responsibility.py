# A chain of components who all get the change to process a command or a query,
# optionally having a default processing implementation,
# and an ability to terminate the processing chain

class Creature:
    def __init__(self, game, attack, defence):
        self.game = game
        self._attack = attack
        self._defense = defence

    @property
    def attack(self):
        return self._attack

    @property
    def defense(self):
        return self._defense

    def __str__(self):
        return f"{self.__class__.__name__} ({self.attack}/{self.defense})"

class Goblin(Creature):
    def __init__(self, game, attack=1, defense=1):
        super().__init__(game, attack, defense)

    @property
    def attack(self):
        attack = super().attack
        for c in self.game.creatures:
            if isinstance(c, GoblinKing) and c is not self:
                attack += 1
        return attack

    @property
    def defense(self):
        defense = super().defense
        defense = len(self.game.creatures)
        return defense


class GoblinKing(Goblin):
    def __init__(self, game):
        super().__init__(game, attack=3, defense=3)


class Game:
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

    print(goblin1)
    print(goblin2)
    print(goblin3)
    print(king_goblin)