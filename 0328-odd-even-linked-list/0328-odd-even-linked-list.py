# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        odd = head
        even = head.next
        evenHead = head.next
        
        if not even.next:
            return head
        
        while odd and even:
            nex = even.next
            odd.next = nex
            podd = odd
            odd = odd.next
            if nex:
                even.next = nex.next
                even = even.next
        if not odd:
            podd.next = evenHead
        else:
            odd.next = evenHead
        
        return head
                
            
            
            
        