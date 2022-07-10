class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        
        numSet = set(nums)
        
        for num in nums:
            if num-1 not in numSet:
                nextNum = num+1
                currSeq = 1

                while nextNum in numSet:
                    nextNum += 1
                    currSeq += 1

                res = max(res, currSeq)
        
        return res