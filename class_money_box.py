class MoneyBox:
  def __init__(self,capacity):
    self.val = 0
    self.capacity = capacity
  def can_add(self, v):
    if self.val + v <= self.capacity:
      return True
    else:
      return False
  def add(self, v):
    self.val += v