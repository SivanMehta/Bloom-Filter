import unittest

class Bloom_Filter():
    def __init__(self):
        self.contents_array = []
        self.contents_set = ()

        self.filter = 0

    def add(self, word):
        self.filter = self.hash_word(word)

    def contains(self, word):
        bloom_filter = self.filter
        in_question = self.hash_word(word)

        while(bloom_filter >= 1):
            if bloom_filter % 2 != in_question % 2: return False
            
            bloom_filter /= 2
            in_question /= 2

        return True


    def hash_word(self, word):
        return self.filter | ((self.hash_sum(word) << 10) + self.hash_length(word))

    def hash_length(self, word):
        return len(word)

    def hash_sum(self, word):
        total = 0
        for char in word:
            total += ord(char)
        return total

class TestFilterMethods(unittest.TestCase):

    def setUp(self):
        # named after my 9th grade bio teacher, Arthur Bloom
        
        self.arthur = Bloom_Filter()

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
        self.assertEqual(self.arthur.filter,     0b00010110100000000001)
        self.arthur.add("\x01")
        self.assertEqual(self.arthur.filter,     0b00010110110000000001)
        self.arthur.add("Z\x01")
        self.assertEqual(self.arthur.filter,     0b00010110110000000011)
        self.arthur.add("frank")
        self.assertEqual(self.arthur.filter,     0b10010110110000000111)

    def test_contains(self):
        self.arthur.add("Z")
        self.assertTrue(self.arthur.contains("Z"))
        self.arthur.add("\x01")
        self.assertTrue(self.arthur.contains("\x01"))
        self.arthur.add("Z\x01")
        self.assertTrue(self.arthur.contains("Z\x01"))
        self.arthur.add("frank")
        self.assertTrue(self.arthur.contains("frank"))

        self.assertFalse(self.arthur.contains("My name is"))
        self.assertFalse(self.arthur.contains("none of your business"))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFilterMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
