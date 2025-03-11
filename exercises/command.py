# An object that represents an instruction to perform an action.
# Contains all the information necessary for the action to be taken.

from enum import Enum


class Command:
    """
    Command Pattern: Represents a command object with an action and amount.
    Encapsulates the request to perform an action on the Account.
    """
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, action, amount):
        """Initializes the Command with the action and amount."""
        self.action = action
        self.amount = amount
        self.success = False # Indicates if the command was successful


class Account:
    """
    Command Pattern: Receiver object that performs the actual actions.
    """
    def __init__(self, balance=0):
        """Initializes the Account with a balance."""
        self.balance = balance

    def process(self, command):
        """
        Processes the given Command.
        Updates the account balance and sets the command's success status.
        """
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
    dc = Command(Command.Action.DEPOSIT, 100) # Creates a deposit command
    wc = Command(Command.Action.WITHDRAW, 1000) # Creates a withdraw command
    acc = Account()
    acc.process(dc) # Processes the deposit command
    print(dc.success) # Output: True
    acc.process(wc) # Processes the withdraw command
    print(wc.success) # Output: False
