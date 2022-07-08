class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        zeroCount = {}
        
        total = 1
        
        for num in nums:
            if num == 0:
                if 0 in zeroCount:
                    zeroCount[0] += 1
                else:
                    zeroCount[0] = 1
            else:    
                total *= num
        
        if 0 in zeroCount and zeroCount[0] > 1:
            total = 0
        
        for num in nums:
            
            if num == 0:
                res.append(total)
            elif 0 in zeroCount:
                res.append(0)
            else:
                res.append(int(total/num))
        
        return res