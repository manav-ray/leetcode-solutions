"""

TC - O(n)
SC - O(n)

"""

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        unique = defaultdict(int)

        for n in nums:
            unique[n] += 1
        
        res = 0

        for n, c in unique.items():
            if c == 1:
                res += n

        return res