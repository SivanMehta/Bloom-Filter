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

class TestFilterMethods(unittest.TestCase):

    def setUp(self):
        self.arthur = Filter()

    def test_hash_sum(self):
        self.assertEqual(self.arthur.hash_sum('hello'), 532)
        self.assertEqual(self.arthur.hash_sum('world'), 552)
        self.assertEqual(self.arthur.hash_sum('Sivan'), 513)
        self.assertEqual(self.arthur.hash_sum('Mehta'), 495)
        self.assertEqual(self.arthur.hash_sum(''), 0)

    def test_hash_length(self):
        self.assertEqual(self.arthur.hash_length('Hello!'), 6)
        self.assertEqual(self.arthur.hash_length('My'), 2)
        self.assertEqual(self.arthur.hash_length('name'), 4)
        self.assertEqual(self.arthur.hash_length('is'), 2)
        self.assertEqual(self.arthur.hash_length('none of your business'), 21)

    def test_hash_word(self):
        self.assertEqual(self.arthur.hash_word("Z"),     0b00010110100000000001)
        self.assertEqual(self.arthur.hash_word("\x01"),  0b00000000010000000001)
        self.assertEqual(self.arthur.hash_word("Z\x01"), 0b00010110110000000010)
        self.assertEqual(self.arthur.hash_word("frank"), 0b10000100100000000101)

    def test_add(self):
        self.arthur.add("Z")
        self.assertEqual(self.arthur.bloom_filter,     0b00010110100000000001)
        self.arthur.add("\x01")
        self.assertEqual(self.arthur.bloom_filter,     0b00010110110000000001)
        self.arthur.add("Z\x01")
        self.assertEqual(self.arthur.bloom_filter,     0b00010110110000000011)
        self.arthur.add("frank")
        self.assertEqual(self.arthur.bloom_filter,     0b10010110110000000111)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFilterMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
