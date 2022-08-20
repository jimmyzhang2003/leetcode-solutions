# Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/

# Time Complexity: O(N)
# Space Complexity: O(N)
# (Stack)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for x in tokens:
            if x in '+-*/':
                num2, num1 = int(stack.pop()), int(stack.pop())
                
                if x == '+':
                    stack.append(num1 + num2)
                elif x == '-':
                    stack.append(num1 - num2)
                elif x == '*':
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num1 / num2))         
            else:
                stack.append(x)
        
        return stack.pop()