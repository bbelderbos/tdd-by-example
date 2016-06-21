class Money(object):
  def __init__(self, amount):
    self._amount = amount

  # http://stackoverflow.com/questions/34728569/what-is-assertequal-in-python-unittest-supposed-to-do
  def __eq__(self, other):
    return isinstance(other, Money) and self._amount == other._amount

  def equals(self, Money):
    return Money._amount == self._amount

  def times(self, multiplier):
    return Money(self._amount * multiplier)


class Dollar(Money):
  
  def __init__(self, amount):
    self._amount = amount


class Franc(Money):
  
  def __init__(self, amount):
    self._amount = amount

