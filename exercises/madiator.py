# A component tha facilitates communication between other components
# without them necessary being aware of each other
# or having direct access to each other.

class Mediator:
    def __init__(self):
        self.participants = []

    def broadcast(self, sender, value):
        for participant in self.participants:
            if participant != sender:
                participant.value += value

class Participant:
    def __init__(self, mediator):
        self.value = 0
        self.mediator = mediator
        self.mediator.participants.append(self)

    def say(self, value):
        self.mediator.broadcast(self, value)


if __name__ == '__main__':
    mediator = Mediator()
    p1 = Participant(mediator)
    p2 = Participant(mediator)

    p1.say(3)
    print(f"p1: {p1.value}, p2: {p2.value}")
    p2.say(2)
    print(f"p1: {p1.value}, p2: {p2.value}")