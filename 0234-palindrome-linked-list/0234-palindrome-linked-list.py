# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = slow
        nex = prev.next
        cur = prev.next
        while cur:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        slow.next = None   
        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
            
        return True

        