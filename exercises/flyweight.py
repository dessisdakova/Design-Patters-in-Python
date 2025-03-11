# A space optimization technique that lets us use less memory
# by storing externally the data associated with similar objects.

class Sentence:
    """
    Flyweight Pattern: Represents a sentence with words and their formatting.
    Uses a dictionary to store formatting information externally.
    """
    def __init__(self, plain_text):
        """Initializes the Sentence with plain text."""
        self.plain_text = plain_text
        self.words = self.plain_text.split(" ")
        self.words_formatter = {}

    def __getitem__(self, index):
        """Returns a WordFormatter for the word at the given index."""
        wf = WordFormatter()
        self.words_formatter[index] = wf
        return wf

    def __str__(self):
        """Returns a string representation of the sentence with applied formatting."""
        result = []
        for i, word in enumerate(self.words):
            if i in self.words_formatter and self.words_formatter[i].capitalize:
                result.append(word.upper())
            else:
                result.append(word)
        return " ".join(result)


class WordFormatter:
    """
    Flyweight Pattern: Represents the formatting for a word.
    Stores the formatting state externally.
    """
    def __init__(self):
        """Initializes the WordFormatter with default formatting."""
        self.capitalize = False


if __name__ == '__main__':
    sentence = Sentence('hello world')
    sentence[1].capitalize = True
    print(sentence) # Output: hello WORLD
