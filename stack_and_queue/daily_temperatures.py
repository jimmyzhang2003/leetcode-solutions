# Link: https://leetcode.com/problems/daily-temperatures/

# Time Complexity: O(N)
# Space Complexity: O(N)
# (Monotonic Stack)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in temperatures]
        stack = []

        for i, temp in enumerate(temperatures):
            # compare current temperature to top of stack
            while stack and temp > stack[-1][1]:
                prevIdx, prevTemp = stack.pop()
                res[prevIdx] = i - prevIdx
                
            # push current temperature onto stack
            stack.append((i, temp))

        return res   