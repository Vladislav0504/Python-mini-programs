class Disjoint_sets_park(list):
  d = {}
  def Join(self, j, k):
    if self[j - 1] != self[k - 1]:
      first = self.d[self[j - 1]][0]
      last = self.d[self[k - 1]][1]
      dim_j = (self.d[self[j - 1]][1] + len(self) - self.d[self[j - 1]][0] + 1) % len(self)
      dim_k = (self.d[self[k - 1]][1] + len(self) - self.d[self[k - 1]][0] + 1) % len(self)
      if dim_j > dim_k:
        self[j % len(self)] = self[j - 1]
        j, k = k, j
      else:
        self[j % len(self)] = self[k - 1]
      set_j, set_k = self[j - 1], self[k - 1]
      self.d[set_k][0] = first
      self.d[set_k][1] = last
      m = self.d[self[j - 1]][0] - 1
      for i in range(m, m + min(dim_j, dim_k)):
        self[i % len(self)] = set_k
      self.d.pop(set_j)
  def Parking(self, i):
    if self[i - 1] == 0:
      if self[i - 2] == 0 and self[i % len(self)] == 0:
        self[i - 1] = i
        self.d[i] = [i, i]
      elif self[i - 2] == 0 and self[i % len(self)] != 0:
        self[i - 1] = self[i % len(self)]
        self.d[self[i - 1]][0] = i
      elif self[i - 2] != 0 and self[i % len(self)] == 0:
        self[i - 1] = self[i - 2]
        self.d[self[i - 1]][1] = i
      else:
        if i == 1:
          self.Join(len(self), i + 1)
        elif i > 1 and i < len(self):
          self.Join(i - 1, i + 1)
        else:
          self.Join(i - 1, 1)
      return i
    else:
      if self.d[self[i - 1]][1] <= len(self) - 1:
        place = self.d[self[i - 1]][1] + 1
      else:
        place = 1
      if self[place % len(self)] == 0:
        self[place - 1] = self[i - 1]
        self.d[self[i - 1]][1] = place
      else:
        if place == 1:
          self.Join(len(self), place + 1)
        elif place > 1 and place < len(self):
          self.Join(place - 1, place + 1)
        else:
          self.Join(place - 1, 1)
      return place
n = int(input())
S = Disjoint_sets_park()
S.extend([0] * n)
for el in input().split():
    print(S.Parking(int(el)), end=' ')