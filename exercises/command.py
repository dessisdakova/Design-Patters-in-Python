# An object that represents an instruction to perform an action.
# Contains all the information necessary for the action to be taken.

from enum import Enum


class Command:
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, action, amount):
        self.action = action
        self.amount = amount
        self.success = False


class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def process(self, command):
        if command.action == Command.Action.DEPOSIT:
            self.balance += command.amount
            command.success = True
        elif command.action == Command.Action.WITHDRAW:
            if self.balance >= command.amount:
                self.balance -= command.amount
                command.success = True
            else:
                command.success = False


if __name__ == '__main__':
    dc = Command(Command.Action.DEPOSIT, 100)
    wc = Command(Command.Action.WITHDRAW, 1000)
    acc = Account()
    acc.process(dc)
    print(dc.success)
    acc.process(wc)
    print(wc.success)