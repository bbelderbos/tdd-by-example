from currency import Dollar

import unittest

class testCurrency(unittest.TestCase):
  
  def testMultiplication(self):
    five = Dollar(5)
    self.assertEquals(Dollar(10), five.times(2))
    self.assertEquals(Dollar(15), five.times(3))

  def testEquality(self):
    self.assertTrue(Dollar(5).equals(Dollar(5)))
    self.assertFalse(Dollar(5).equals(Dollar(6)))

if __name__ == "__main__":
  unittest.main()
