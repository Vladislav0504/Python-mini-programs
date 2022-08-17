class NonPositiveError(Exception):
  pass
class PositiveList(list):
  def __init__(self):
    self.lst = []
  def append(self,x):
    if x > 0:
      super(PositiveList, self).append(x)
    else: 
      raise NonPositiveError()