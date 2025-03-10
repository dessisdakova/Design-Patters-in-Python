# A space optimization technique that lets us use less memory
# by storing externally the data associated with similar objects.

class Sentence:
    def __init__(self, plain_text):
        self.plain_text = plain_text
        self.words = self.plain_text.split(" ")
        self.words_formatter = {}

    def __getitem__(self, index):
        wf = WordFormatter()
        self.words_formatter[index] = wf
        return wf

    def __str__(self):
        result = []
        for i, word in enumerate(self.words):
            if i in self.words_formatter and self.words_formatter[i].capitalize:
                result.append(word.upper())
            else:
                result.append(word)
        return " ".join(result)


class WordFormatter:
    def __init__(self):
        self.capitalize = False


if __name__ == '__main__':
    sentence = Sentence('hello world')
    sentence[1].capitalize = True
    print(sentence)