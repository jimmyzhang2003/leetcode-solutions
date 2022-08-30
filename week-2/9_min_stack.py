# Link: https://leetcode.com/problems/min-stack/

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Time Complexity: O(1) for all operations
# Space Complexity: O(N) 
# (Stack) (with stack node))
class MinStackNode:
    
    def __init__(self, val, minVal):
        self.val = val
        self.minVal = minVal

class MinStack:

    def __init__(self):
        self.minVal = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        self.minVal = min(self.minVal, val)
        self.stack.append(MinStackNode(val, self.minVal))

    def pop(self) -> None:
        if self.stack[-1].val == self.minVal:
            self.stack.pop()
            self.minVal = self.stack[-1].minVal if self.stack else float('inf')
        else:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1].val

    def getMin(self) -> int:
        return self.minVal

# Time Complexity: O(1) for all operations
# Space Complexity: O(N) 
# (Stack) (without stack node))
class MinStack:

    def __init__(self):
        self.minVal = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        self.minVal = min(self.minVal, val)
        self.stack.append((val, self.minVal))

    def pop(self) -> None:
        if self.stack[-1][0] == self.minVal:
            self.stack.pop()
            self.minVal = self.stack[-1][1] if self.stack else float('inf')
        else:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.minVal