from currency import Dollar

import unittest

class testCurrency(unittest.TestCase):
  
  def testMultiplication(self):
    five = Dollar(5)
    five.times(2);
    self.assertEquals(10, five.amount);

if __name__ == "__main__":
  unittest.main()
