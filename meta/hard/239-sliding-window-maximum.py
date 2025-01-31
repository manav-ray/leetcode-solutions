"""

Monotonic decreasing stack
 - Elements are irrelevant if (1) larger element comes after it, or (2) it is outside the sliding window
 - Elements are relevant if (1) it is larger than all the elements before since it could be the answer to the current sliding window, and 
    (2) it's smaller than all the elements before since it could be the answer to a following sliding window
 - We use a queue since it is easy and efficient to pop from the left (this represents going out of the sliding window)
 - We keep it monotonic decreasing - While a new elem is larger than the elems before in the queue, keep on popping
                                   - if smaller, just add
 - We also have a left check to make sure we're not keeping track of elements that are outside the sliding window
 - When we do this, the larger element of each sliding window will be at the 0th index of the queue

Time complexity - O(n)
Space compexity - O(k)

"""


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        q = deque()

        for i in range(k):
            while q and q[-1][1] < nums[i]:
                q.pop()
            
            q.append((i, nums[i]))
        
        res.append(q[0][1])

        l, r = 1, k

        while r < len(nums):
            while q and q[-1][1] < nums[r]:
                q.pop()
            
            while q and q[0][0] < l:
                q.popleft()
            q.append((r, nums[r]))
            res.append(q[0][1])

            l += 1
            r += 1


        return res