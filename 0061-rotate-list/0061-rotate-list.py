# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        l = 1
        tail = head
        while tail.next:
            tail = tail.next
            l+=1
        temp = head
        
        k = k % l
        
        if not k:
            return head
        
        for i in range(l-k-1):
            temp = temp.next
        
        res = temp.next
        temp.next = None
        
        tail.next = head
        
        return res