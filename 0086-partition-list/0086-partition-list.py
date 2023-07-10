# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        l = ListNode()
        r = ListNode()
        s = l
        point = r
        temp = head
        while temp:
            if temp.val < x:
                l.next = ListNode(temp.val)
                l = l.next
            else:
                r.next = ListNode(temp.val)
                r = r.next
            temp = temp.next
        

        l.next = point.next
        
        return s.next