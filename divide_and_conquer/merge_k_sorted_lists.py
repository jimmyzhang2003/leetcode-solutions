# Link: https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time Complexity: O(N log K)
# Space Complexity: O(log K)
# (Divide and Conquer)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(node1, node2):
            head = curr = ListNode()

            while node1 and node2:
                if node1.val < node2.val:
                    curr.next = node1
                    node1 = node1.next
                else:
                    curr.next = node2
                    node2 = node2.next

                curr = curr.next

            # append remaining nodes if one list is shorter than the other
            curr.next = node1 or node2

            return head.next
        
        # base cases
        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        # divide and conquer
        half1 = self.mergeKLists(lists[:len(lists)//2])
        half2 = self.mergeKLists(lists[len(lists)//2:])

        return merge(half1, half2)