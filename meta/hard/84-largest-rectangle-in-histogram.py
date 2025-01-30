"""

Monotonic increasing stack:
 - A rectangle can contribute to an area as long as it is shorter than the rectangles that come after it.
 - So, we use a stack to keep track of rectangles in increasing order.
 - Add curr index + height to stack if larger than rectangle before.
 - Keep on popping from stack while current height is smaller than heights before (monotonic).
    - With every pop, calculate the area -> popped height * (curr index - popped index)
- The index stored in the stack doesn't represent the current index of the height, but rather the index of the last rectangle that is either the same height or taller.
    - We keep track of this since this rectangle can contribute to the current rectangle's area (not a bottleneck).  
- After all of this is done, it's still possible that the stack has elements since they would be in increasing order.
    - Calculate area of these elements in a similar way -> popped_height * (len of heights - popped index)


Time complexity - O(n)
Space complexity - O(n) 

"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []

        for i, height in enumerate(heights):

            curr_start = i
            while stack and height < stack[-1][1]:
                popped_idx, popped_height = stack.pop()
                res = max(res, popped_height * (i - popped_idx))
                curr_start = popped_idx

            stack.append((curr_start, height))
        

        while stack:
            popped_idx, popped_height = stack.pop()
            res = max(res, popped_height * (len(heights) - popped_idx))


        return res