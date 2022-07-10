class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        
        nums.sort()
        
        for i in range(len(nums)):
            
            start = i+1
            end = len(nums) - 1
            
            while start < end:
                currSum = nums[start] + nums[end] + nums[i]
                if currSum == 0:
                    res.add(tuple([nums[i], nums[start], nums[end]]))
                    start += 1
                    end -= 1
                elif currSum < 0:
                    start += 1
                else:
                    end -= 1
                
        
        return list(res)