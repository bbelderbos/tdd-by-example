class Money(object):
  def __init__(self, amount):
    self._amount = amount

  # http://stackoverflow.com/questions/34728569/what-is-assertequal-in-python-unittest-supposed-to-do
  def __eq__(self, other):
    return isinstance(other, Money) and self._amount == other._amount

  def equals(self, Money, v=False):
    return Money._amount == self._amount and Money.__class__ == self.__class__

  def times(self, multiplier):
    return Money(self._amount * multiplier)

  @classmethod
  def dollar(self, amount):
    return Dollar(amount)

  @classmethod
  def franc(self, amount):
    return Franc(amount)


class Dollar(Money):
  
  def __init__(self, amount):
    self._amount = amount


class Franc(Money):
  
  def __init__(self, amount):
    self._amount = amount

if __name__ == "__main__":
  m = Money(10)
  print m.__class__
  d = Dollar(5)
  print d.__class__
