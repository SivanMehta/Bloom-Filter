import unittest

class Filter():
    def __init__(self):
        self.contents_array = []
        self.contents_set = ()

        self.bloom_filter = 0

    def add(self, word):
        self.bloom_filter = self.hash_word(word)

    def contains(self, word): pass

    def hash_word(self, word):
        return self.bloom_filter | ((self.hash_sum(word) << 10) + self.hash_length(word))

    def hash_length(self, word):
        return len(word)

    def hash_sum(self, word):
        total = 0
        for char in word:
            total += ord(char)
        return total