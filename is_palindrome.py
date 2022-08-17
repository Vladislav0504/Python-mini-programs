class Solution:
  def isPalindrome(self, head: ListNode, tail: ListNode) -> bool:
    while head != None:
      if head.val == tail.val:
      	head = head.next
      	tail = tail.prev
      else:
      	return False
    return True