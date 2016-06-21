from currency import Dollar, Franc

import unittest

class testCurrency(unittest.TestCase):
  
  def testMultiplication(self):
    five = Dollar(5)
    self.assertEquals(Dollar(10), five.times(2))
    self.assertEquals(Dollar(15), five.times(3))

  def testEquality(self):
    self.assertTrue(Dollar(5).equals(Dollar(5)))
    self.assertFalse(Dollar(5).equals(Dollar(6)))
    self.assertTrue(Franc(5).equals(Franc(5)))
    self.assertFalse(Franc(5).equals(Franc(6)))
    self.assertFalse(Franc(5).equals(Dollar(5)))

  def testFrancMultiplication(self):
    five = Franc(5)
    self.assertEquals(Franc(10), five.times(2))
    self.assertEquals(Franc(15), five.times(3))

if __name__ == "__main__":
  unittest.main()
