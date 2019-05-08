import unittest
from NijenhuisAlgorithm.nijenhuis import *


class TestNijenhuis(unittest.TestCase):

    def test_nijenhuis(self):
        self.assertEqual(nijenhuis(3, 25), 47)
        self.assertEqual(nijenhuis(6, 9, 20), 43)


if __name__ == '__main__':
    unittest.main()
