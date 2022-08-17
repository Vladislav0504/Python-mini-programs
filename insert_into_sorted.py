class Solution:
  def insertIntoSorted(self, head: ListNode, new_value: int) -> ListNode:
    prev = None
    v = head
    while v != None and v.val > new_value:
      prev = v
      v = v.next
    if v == head:
      head = ListNode(new_value)
      head.next = v
    else:
      prev.next = ListNode(new_value)
      prev.next.next = v
    return head