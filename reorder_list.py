class Solution:
  def reorderList(self, head: ListNode, tail: ListNode) -> ListNode:
    v = head
    while head != tail and head.next != tail:
      s1, s2 = head.next, tail.prev
      head.next = tail
      tail.prev = head
      tail.next = s1
      s1.prev = tail
      s2.next = None
      head, tail = s1, s2
    return v