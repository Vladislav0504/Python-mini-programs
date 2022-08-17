class Buffer:
  def __init__(self):
    self.lst = []
    self.sum = 0
    self.len = 0
  def add(self, *a):
    l = len(a)
    k = (self.len + l) // 5
    j = 0
    for i in range(k):
      while self.len < 5:
        self.len += 1
        self.sum += a[j]
        j += 1
      print(self.sum)
      self.lst = []
      self.sum = 0
      self.len = 0
    for i in range(j,l):
      self.lst.append(a[i])
      self.len += 1
      self.sum += a[i]
  def get_current_part(self):
    return self.lst