# Name : Dhairya Chaudhary
# Roll No : 2019035
# Group : 8

import unittest
from a1 import changeBase

# TEST cases should cover the different boundary cases.

class testpoint(unittest.TestCase):

    def test_change_base(self):
        self.assertAlmostEqual(changeBase(1, "INR", "GBP", "2010-10-25"), 0.0135508231, delta = 0.1)
        self.assertAlmostEqual(changeBase(100000, "RON", "CHF", "2019-10-01"), 22954.6841784, delta = 1)
        self.assertAlmostEqual(changeBase(0, "CAD", "CZK", "2010-10-18"), 0.0, delta = 0)
        self.assertAlmostEqual(changeBase(12, "DKK", "LVL", "2012-07-14"), 1.12296834039, delta = 0.1)
        self.assertAlmostEqual(changeBase(20, "HRK", "KRW", "2010-10-25"), 4265.97469113, delta = 0.1)
        self.assertAlmostEqual(changeBase(15, "EUR", "HUF", "2013-10-25"), 4392.3, delta = 0.1)
        self.assertAlmostEqual(changeBase(30, "TRY", "EUR", "2018-02-25"), 6.44122383253, delta = 0.5)
        self.assertAlmostEqual(changeBase(13.7514, "JPY", "PLN", "2015-04-15"), 0.4366928147, delta = 0.1)
        self.assertAlmostEqual(changeBase(0.1, "ZAR", "USD", "2017-11-22"), 0.00720399779, delta = 0.1)
        self.assertAlmostEqual(changeBase(0.005, "NZD", "IDR", "2016-06-02"), 46.3421755494, delta = 0.01)


if __name__=='__main__':
	unittest.main()
