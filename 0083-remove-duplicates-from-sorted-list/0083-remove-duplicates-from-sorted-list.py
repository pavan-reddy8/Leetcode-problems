# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        while cur:
            if prev and cur.val == prev.val:
                prev.next = cur.next
                cur = cur.next

            else:
                prev = cur
                cur = cur.next
        return head