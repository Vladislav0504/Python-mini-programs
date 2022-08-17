class Solution:
  def deleteDuplicates(self, head: ListNode) -> ListNode:
    prev = None
    v = head
    while v != None:
      if prev != None and prev.val == v.val:
      	prev.next = v.next
      else:
      	prev = v
      v = v.next
    return head