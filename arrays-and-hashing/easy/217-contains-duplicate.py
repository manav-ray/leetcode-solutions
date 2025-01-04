class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         dupe_check = set()

         for n in nums:
            if n in dupe_check:
                return True
            
            dupe_check.add(n)

         return False