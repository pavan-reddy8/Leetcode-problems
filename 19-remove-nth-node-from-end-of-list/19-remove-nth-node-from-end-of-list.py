# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        l = 0
        while temp:
            l += 1
            temp = temp.next

        temp = head
        pos = l - n
        if pos:
            i = 0
            while i < pos-1:
                temp = temp.next
                i+=1
            temp.next = temp.next.next
        else:
            head = head.next
        return head
            