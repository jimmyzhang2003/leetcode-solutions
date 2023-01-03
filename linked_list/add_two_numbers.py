# Link: https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time Complexity: O(max(N + M))
# Space Complexity: O(max(N + M))
# (Linked List)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = curr = ListNode()
        carry = 0

        while l1 or l2:
            curr.next = ListNode()
            curr = curr.next

            if not l1:
                curr.val = l2.val + carry
                l2 = l2.next 
            elif not l2:
                curr.val = l1.val + carry
                l1 = l1.next
            else:
                curr.val = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next

            carry = curr.val // 10
            curr.val %= 10

        if carry:
            curr.next = ListNode(1)

        return head.next