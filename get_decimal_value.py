class Solution:
  def getDecimalValue(self, head: ListNode) -> int:
    numb = []
    while head != None:
      numb.append(head.val)
      head = head.next
    s = 0
    for i in range(len(numb)):
      s += numb[i] * 2 ** (len(numb) - 1 - i)
    return s 