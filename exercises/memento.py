# A token/handle representing the system state.
# Lets us roll back to the state when the token was generated.
# May or may not directly expose state information.

class Token:
    def __init__(self, value=0):
        self.value = value

    def __str__(self):
        return str(self.value)

class Memento(list):
    pass

class TokenMachine:
    def __init__(self):
        self.tokens = []

    def add_token_value(self, value):
        return self.add_token(Token(value))

    def add_token(self, token):
        # Create a deep copy of the tokens list to create the memento
        self.tokens.append(token)
        memento = Memento([Token(t.value) for t in self.tokens])
        return memento

    def revert(self, memento):
        # Restore the tokens list from the memento, creating new Token instances
        self.tokens = [Token(t.value) for t in memento]


if __name__ == '__main__':
    tm = TokenMachine()
    m1 = tm.add_token_value(1)
    print(f"Tokens after m1: {[str(t) for t in tm.tokens]}")
    m2 = tm.add_token_value(2)
    print(f"Tokens after m2: {[str(t) for t in tm.tokens]}")
    tm.revert(m1)
    print(f"Tokens after reverting to m1: {[str(t) for t in tm.tokens]}")
    token = Token(3)
    m3 = tm.add_token(token)
    print(f"Tokens after m3: {[str(t) for t in tm.tokens]}")
    token.value = 4
    print(f"Tokens after changing the value of token: {[str(t) for t in tm.tokens]}")
    tm.revert(m3)
    print(f"Tokens after reverting to m3: {[str(t) for t in tm.tokens]}")