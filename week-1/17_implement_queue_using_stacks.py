# Link: https://leetcode.com/problems/implement-queue-using-stacks/

# Time Complexity: O(1) for all operations, O(1) amortized for pop
# Space Complexity: O(N)
# (Stack/Queue)
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if self.stack2:
            return self.stack2.pop()
        
        while self.stack1:
            self.stack2.append(self.stack1.pop())
            
        return self.stack2.pop()

    def peek(self) -> int:
        if self.stack2:
            return self.stack2[-1]
        return self.stack1[0]
        
    def empty(self) -> bool:
        return len(self.stack1) + len(self.stack2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()