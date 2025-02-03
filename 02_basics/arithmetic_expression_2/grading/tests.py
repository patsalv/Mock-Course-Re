#!/usr/bin/env python3

# Scaffolding necessary to set up ACCESS test
import sys
try: from universal.harness import *
except: sys.path.append("../../universal/"); from harness import *

# Grading test suite starts here

script = grading_import("task", "script")

class GradingTests(AccessTestCase):

    def _test(self, a, b, c, expected):
        actual = script.calculateX(a, b, c)
        self.hint("Calculation not correct for a={}, b={}, c={},... expected result is {}!".format(a, b, c, expected))
        self.assertAlmostEqual(expected[0], actual[0], 5)
        self.assertAlmostEqual(expected[1], actual[1], 5)

    def test_case1(self):
        self.hint("thats a hint")
        self._test(1, 5, 2, (-2.438447,-4.56155))

    def test_case2(self):
        self._test(1, 2, 1, (-1,-1))

TestRunner().run(AccessTestSuite(1, [GradingTests]))
