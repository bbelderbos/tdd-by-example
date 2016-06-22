from currency import Money, Dollar, Franc

import unittest

class testCurrency(unittest.TestCase):
  
  def testMultiplication(self):
    five = Money.dollar(5)
    self.assertEquals(Money.dollar(10), five.times(2))
    self.assertEquals(Money.dollar(15), five.times(3))

  def testEquality(self):
    self.assertTrue(Money.dollar(5).equals(Money.dollar(5)))
    self.assertFalse(Money.dollar(5).equals(Money.dollar(6)))
    self.assertTrue(Money.franc(5).equals(Money.franc(5)))
    self.assertFalse(Money.franc(5).equals(Money.franc(6)))
    self.assertFalse(Money.franc(5).equals(Money.dollar(5)))

  def testFrancMultiplication(self):
    five = Money.franc(5)
    self.assertEquals(Money.franc(10), five.times(2))
    self.assertEquals(Money.franc(15), five.times(3))

  def testCurrency(self):
    self.assertEquals("USD", Money.dollar(1).currency())
    self.assertEquals("CHF", Money.franc(1).currency())

  def testDifferentClassEquality(self):
    self.assertTrue(Money(10, "CHF").equals(Franc(10, "CHF")))

if __name__ == "__main__":
  unittest.main()
