# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, h: Optional[ListNode]) -> Optional[ListNode]:
        head = h
        temp = head
        while head is not None:
            prev = head
            head= head.next
            while head and temp.val == head.val:
                prev.next = head.next
                head= head.next
            temp = head
                
        return h