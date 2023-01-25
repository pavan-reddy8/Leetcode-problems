# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        left = head
        right = self.mid(head)
        temp = right.next
        right.next = None
        right = temp
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left,right)
    
    def mid(self,h):
        slow = h
        fast = h.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(slef,left,right):
        temp = ListNode(0)
        res = temp
        while left and right:
            if left.val < right .val:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next
        if left :
            temp.next = left
        if right:
            temp.next = right
        return res.next
        
        