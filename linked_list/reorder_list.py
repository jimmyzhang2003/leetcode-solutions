# Link: https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time Complexity: O(N)
# Space Complexity: O(N)
# (Linked List with Deque)
from collections import deque

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr = head.next
        nodes = deque([])

        while curr:
            nodes.append(curr)
            curr = curr.next
            
        prev = head

        while nodes:
            if len(nodes) == 1:
                final = nodes.pop()
                final.next = None
                prev.next = final
                break

            second, first = nodes.popleft(), nodes.pop()
            
            prev.next = first
            first.next = second
            second.next = None
            prev = second

# Time Complexity: O(N)
# Space Complexity: O(1)
# (Linked List with Two Pointers)
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the middle of the linked list
        slow, fast = head, head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse the second half of the linked list
        curr = slow.next
        prev = slow.next = None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # merge the two linked lists
        while prev:
            tmp, tmp2 = head.next, prev.next
            head.next = prev
            prev.next = tmp

            head, prev = tmp, tmp2