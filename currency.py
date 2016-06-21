class Money(object):
  # http://stackoverflow.com/questions/34728569/what-is-assertequal-in-python-unittest-supposed-to-do
  def __eq__(self, other):
    return isinstance(other, Money) and self._amount == other._amount


class Dollar(Money):
  
  def __init__(self, amount):
    self._amount = amount

  def times(self, multiplier):
    return Dollar(self._amount * multiplier)
  
  def equals(self, Dollar):
    return Dollar._amount == self._amount


class Franc(Money):
  
  def __init__(self, amount):
    self._amount = amount

  def times(self, multiplier):
    return Franc(self._amount * multiplier)
  
  def equals(self, Franc):
    return Franc._amount == self._amount
