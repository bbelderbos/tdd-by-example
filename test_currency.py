from currency import Dollar

import unittest

class testCurrency(unittest.TestCase):
  
  def testMultiplication(self):
    five = Dollar(5)
    product = five.times(2)
    self.assertEquals(10, product.amount)
    product = five.times(3)
    self.assertEquals(15, product.amount)

  def testEquality(self):
    self.assertTrue(Dollar(5).equals(Dollar(5)))
    self.assertFalse(Dollar(5).equals(Dollar(6)))

if __name__ == "__main__":
  unittest.main()
