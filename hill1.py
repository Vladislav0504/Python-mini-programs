import sys
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None
    self.prev = None
class List:
  def __init__(self):
    self.head = None
    self.tail = None
  def Insert1(self, x):
    if self.head is None:
      self.head = ListNode(x)
      self.tail = self.head
    else:
      v = self.head
      v.prev = ListNode(x)
      v.prev.next = v
      self.head = v.prev
  def Insert2(self, x):
    if self.head is None:
      self.head = ListNode(x)
      self.tail = self.head
    else:
      v = self.tail
      v.next = ListNode(x)
      v.next.prev = v
      self.tail = v.next
  def Delete1(self):
  	self.head = self.head.next
  	if self.head != None:
  	  self.head.prev = None
  	else:
  	  self.tail = None
  def Delete2(self):
  	self.tail = self.tail.prev
  	if self.tail != None:
  	  self.tail.next = None
  	else:
  	  self.head = None
n = int(input())
lst1, lst2 = List(), List()
i, l1, l2 =  0, 0, 0
for line in sys.stdin:
  el = line.split()
  if el[0] == 's':
  	lst2.Insert2(el[1])
  	l2 += 1
  elif el[0] == '+':
    print(lst1.head.val)
    lst1.Delete1()
    l1 -= 1
  elif el[0] == 'c':
  	lst1.Insert1(el[1])
  	l1 += 1
  else:
    if l1 == l2:
      lst1.Insert2(el[1])
      l1 += 1
    else:
      lst2.Insert1(el[1])
      l2 += 1
  if l1 < l2:
  	lst1.Insert2(lst2.head.val)
  	l1 += 1
  	lst2.Delete1()
  	l2 -= 1
  elif l1 > l2 + 1:
  	lst2.Insert1(lst1.tail.val)
  	lst1.Delete2()
  	l2 += 1
  	l1 -= 1
  i += 1
  if i == n:
  	break