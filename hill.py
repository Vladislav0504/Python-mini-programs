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
    lst1.head = lst1.head.next
    if lst1.head != None:
      lst1.head.prev = None
    else:
      lst1.tail = None
    l1 -= 1
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
  	lst2.head = lst2.head.next
  	if lst2.head != None:
  	  lst2.head.prev = None
  	else:
  	  lst2.tail = None
  	l2 -= 1
  i += 1
  if i == n:
  	break