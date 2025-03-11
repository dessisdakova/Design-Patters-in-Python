# A component tha facilitates communication between other components
# without them necessary being aware of each other
# or having direct access to each other.

class Mediator:
    """
    Mediator Pattern: Facilitates communication between participants.
    Maintains a list of participants and broadcasts messages.
    """
    def __init__(self):
        """Initializes the mediator with an empty list of participants."""
        self.participants = []

    def broadcast(self, sender, value):
        """Broadcasts a value to all participants except the sender."""
        for participant in self.participants:
            if participant != sender:
                participant.value += value

class Participant:
    """
    Mediator Pattern: Represents a participant in the communication.
    """
    def __init__(self, mediator):
        """Initializes the participant with a mediator and initial value."""
        self.value = 0
        self.mediator = mediator
        self.mediator.participants.append(self)

    def say(self, value):
        """Sends a value to the mediator for broadcasting."""
        self.mediator.broadcast(self, value)


if __name__ == '__main__':
    mediator = Mediator()
    p1 = Participant(mediator)
    p2 = Participant(mediator)

    p1.say(3)
    print(f"p1: {p1.value}, p2: {p2.value}") # Output: p1: 0, p2: 3
    p2.say(2)
    print(f"p1: {p1.value}, p2: {p2.value}") # Output: p1: 2, p2: 3
