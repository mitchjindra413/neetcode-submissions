# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = head
        fast = head.next
        while fast and fast.next:
            mid = mid.next
            fast = fast.next.next
        
        
        cur = mid.next
        prev = None
        mid.next = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        org_head = head
        rev_head = prev
        while rev_head:
            tmp1 = org_head.next
            tmp2 = rev_head.next
            org_head.next = rev_head
            rev_head.next = tmp1
            org_head = tmp1
            rev_head = tmp2
        
        


