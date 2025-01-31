"""

Monotonic DECREASING stack

Time complexity - O(n)
Space complexity - O(n)

"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                idx, _ = stack.pop()
                ans[idx] = (i - idx)

            stack.append((i, t)) 


        return ans