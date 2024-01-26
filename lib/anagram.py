# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, words):
        return [w for w in words if sorted(w.lower()) == sorted(self.word) and w.lower() != self.word]

# Example usage:
if __name__ == "__main__":
    word_to_check = "listen"
    possible_anagrams = ['enlists', 'google', 'inlets', 'banana']

    anagram_instance = Anagram(word_to_check)
    result = anagram_instance.match(possible_anagrams)

    print(result)