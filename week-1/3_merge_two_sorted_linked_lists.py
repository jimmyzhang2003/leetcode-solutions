# Link: https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time Complexity: O(N+M)
# Space Complexity: O(N+M)
# (Linked List)
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode: 
        head = ListNode()
        p = head
        
        while l1 or l2:
            if l1 and l2:
                if l1.val > l2.val:
                    p.next = l2
                    l2 = l2.next
                else:
                    p.next = l1
                    l1 = l1.next
                p = p.next
            elif l1:
                p.next = l1
                l1 = l1.next
                p = p.next
            else:
                p.next = l2
                l2 = l2.next
                p = p.next
    
        return head.next