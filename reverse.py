class Solution:
  def reverse(self, head: ListNode) -> ListNode:
    prev = None
    while head.next != None:
      t, head.next = head.next, prev
      prev, head = head, t
    if head.next is None:
      head.next = prev
    return head