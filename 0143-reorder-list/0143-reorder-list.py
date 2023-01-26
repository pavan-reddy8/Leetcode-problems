# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next        
        sec = slow.next
        slow.next = None
        
        prev = None
        while sec:
            temp = sec.next
            sec.next = prev
            prev = sec
            sec = temp
        
        sec = prev
        # print(sec,head)
        cur = head
        while cur and sec:
            nex = cur.next
            cur.next = sec
            temp = sec
            sec = sec.next
            temp.next = nex
            cur = nex
        
        