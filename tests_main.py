import unittest
from main import read_file, _min, _max, _sum, _mult


class Tests(unittest.TestCase):
    f = [3, 4, 5, 6]

    def test__read(self):
        self.assertEqual(read_file('test.txt'), self.f)

    def test__min(self):
        self.assertEqual(_min(read_file('test.txt')), 3)

    def test__max(self):
        self.assertEqual(_max(read_file('test.txt')), 6)

    def test__sum(self):
        self.assertEqual(_sum(read_file('test.txt')), 18)

    def test__mult(self):
        self.assertEqual(_mult(read_file('test.txt')), 3601)



