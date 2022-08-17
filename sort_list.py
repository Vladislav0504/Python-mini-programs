class Solution:
  def sortList(self, head: ListNode) -> ListNode:
    v = head
    end = None
    while v != end:
      while v.next != end:
        if v.val > v.next.val:
          v.val, v.next.val = v.next.val, v.val
        v = v.next
      end = v
      v = head
    return head