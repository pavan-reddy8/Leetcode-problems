# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = list1
        h2 = list2
        res = ListNode()
        l=res
        if not h1 and not h2 :
            return None
        if not h1 or not h2 :
            return h1 or h2
        while h1  and h2:
            if h1.val<= h2.val:
                l.val = h1.val
                h1=h1.next
            else:
                l.val = h2.val
                h2=h2.next
            new = ListNode()
            l.next =new
            l = new

        if h1 or h2 :
            if h1:
                l.val = h1.val
                l.next = h1.next
            else:
                l.val = h2.val
                l.next = h2.next
                
        return res