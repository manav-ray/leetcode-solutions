class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set(nums)

        for n in nums:
            if n-1 not in num_set:
                next_num = n+1

                seq = 1
                while next_num in num_set:
                    next_num += 1
                    seq += 1


                res = max(res, seq) 


        return res