# Link: https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time Complexity: O(N)
# Space Complexity: O(1) 
# (Linked List (Iterative))
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
            
        return prev

# Time Complexity: O(N)
# Space Complexity: O(N) 
# (Linked List (Recursive))
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseListRecursive(head, prev):
            if not head:
                return prev
            
            tmp = head.next
            head.next = prev
            
            return reverseListRecursive(tmp, head)
    
        return reverseListRecursive(head, None)