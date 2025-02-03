from unittest import TestCase

from task import script

class PublicTestSuite(TestCase):

    def test_1234(self):
        actual = script.calculateX(1,5,2)
        expected = (-0.438447,-4.56155)
        self.assertAlmostEqual(expected, actual, 5)

