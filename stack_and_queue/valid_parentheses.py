# Link: https://leetcode.com/problems/valid-parentheses/

# Time Complexity: O(N)
# Space Complexity: O(N)
# (Stack)
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')':'(', '}':'{', ']':'['}
        stack = []
        
        for bracket in s:
            if bracket in '({[':
                stack.append(bracket)
            elif len(stack) == 0 or stack.pop() != mapping[bracket]:
                return False
        
        return len(stack) == 0