from currency import Dollar

import unittest

class testCurrency(unittest.TestCase):
  
  def testMultiplication(self):
    five = Dollar(5);
    product = five.times(2);
    self.assertEquals(10, product.amount);
    product = five.times(3);
    self.assertEquals(15, product.amount);

if __name__ == "__main__":
  unittest.main()
