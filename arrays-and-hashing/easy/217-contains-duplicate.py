class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checker = set()
        
        for i in nums:
            if i in checker:
                return True
            checker.add(i)
        
        return False