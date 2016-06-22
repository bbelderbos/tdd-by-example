import abc

class Money(object):
  def __init__(self, amount, currency):
    self._amount = amount
    self._currency = currency

  # http://stackoverflow.com/questions/34728569/what-is-assertequal-in-python-unittest-supposed-to-do
  def __eq__(self, other):
    return isinstance(other, Money) and self._amount == other._amount

  def equals(self, Money, v=False):
    return Money._amount == self._amount and Money.__class__ == self.__class__

  def times(self, multiplier):
    return Money(self._amount * multiplier, None)

  @classmethod
  def dollar(self, amount):
    return Dollar(amount, "USD")

  @classmethod
  def franc(self, amount):
    return Franc(amount, "CHF")

  def currency(self):
    return self._currency


class Dollar(Money):
  
  def __init__(self, amount, currency):
    super(Dollar, self).__init__(amount, currency)


class Franc(Money):
  
  def __init__(self, amount, currency):
    super(Franc, self).__init__(amount, currency)


if __name__ == "__main__":
  m = Money(10, "USD")
  print m.__class__
  d = Dollar(5, "USD")
  print d.__class__
