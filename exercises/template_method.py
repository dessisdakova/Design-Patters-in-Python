# Allows us to define the "skeleton" of the algorithm
# with concrete implementations defined in subclasses.

from abc import ABC

class Creature:
    def __init__(self, attack, health):
        self.health = health
        self.attack = attack

class CardGame(ABC):
    def __init__(self, creatures):
        self.creatures = creatures

    # return -1 if both creatures alive or both dead after combat
    # otherwise, return the _index_ of winning creature
    def combat(self, c1_index, c2_index):
        c1 = self.creatures[c1_index]
        c2 = self.creatures[c2_index]
        self.hit(c1, c2)
        self.hit(c2, c1)

        if c1.health <= 0 and c2.health <= 0:
            return -1
        elif c1.health > 0 and c2.health > 0:
            return -1
        elif c1.health > 0:
            return c1_index
        else:
            return c2_index


    def hit(self, attacker, defender):
        pass  # implement this in derived classes


class TemporaryDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        if attacker.attack >= defender.health:
            defender.health = 0


class PermanentDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        defender.health -= attacker.attack


if __name__ == '__main__':
    creatures = [Creature(1,2), Creature(1,3),
                 Creature(2,2), Creature(2,2)]

    print("Temporary damage:")
    td = TemporaryDamageCardGame(creatures)
    print("Winner after first round: ", td.combat(0, 1))
    print(f"c1: Health: {creatures[0].health} | Attack: {creatures[0].attack}")
    print(f"c2: Health: {creatures[1].health} | Attack: {creatures[1].attack}")
    print("-----------------------------------")
    print("Permanent damage:")
    td = PermanentDamageCardGame(creatures)
    print("Winner after first round: ", td.combat(0, 1))
    print(f"c1: Health: {creatures[0].health} | Attack: {creatures[0].attack}")
    print(f"c2: Health: {creatures[1].health} | Attack: {creatures[1].attack}")
    print("Winner after second round: ", td.combat(0, 1))
    print(f"c1: Health: {creatures[0].health} | Attack: {creatures[0].attack}")
    print(f"c2: Health: {creatures[1].health} | Attack: {creatures[1].attack}")
    print("-----------------------------------")
    print("Permanent damage:")
    td = PermanentDamageCardGame(creatures)
    print("Winner after first round: ", td.combat(2, 3))
    print(f"c3: Health: {creatures[2].health} | Attack: {creatures[2].attack}")
    print(f"c4: Health: {creatures[3].health} | Attack: {creatures[3].attack}")