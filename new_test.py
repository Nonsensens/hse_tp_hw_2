import unittest
from main import file_is_empty


class TestNew(unittest.TestCase):
    def test__file_is_empty(self):
        self.assertNotEqual(file_is_empty('test.txt'), 0)
