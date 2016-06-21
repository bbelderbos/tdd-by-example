class Dollar:
  
  def __init__(self, amount):
    self._amount = amount

  # http://stackoverflow.com/questions/34728569/what-is-assertequal-in-python-unittest-supposed-to-do
  def __eq__(self, other):
    return isinstance(other, Dollar) and self._amount == other._amount

  def times(self, multiplier):
    return Dollar(self._amount * multiplier)
  
  def equals(self, Dollar):
    return Dollar._amount == self._amount
