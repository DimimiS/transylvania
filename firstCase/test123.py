import unittest

from subtractor import sub

class TestClass(unittest.TestCase):
    def testPos(self):
        self.assertEqual(sub(34,5),"POSITIVE")
    def testNeg(self):
        self.assertEqual(sub(3,5),"NEGATIVE")

unittest.main()