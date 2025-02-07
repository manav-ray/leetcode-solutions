"""

Don't think about the pivot, just think about where M lies:
 - if nums[m] == nums[l], we can't do bs since m could be in either left or right sorted array.
 - if nums[m] > nums[l], that means we're still increasing from l-m -> left sorted array
 - if not, that means we're in right sorted array

TC - O(n) worse O(logn) best
SC - O(1)
 
"""

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target: return True

            if nums[l] == nums[m]:
                l += 1 # Can't do binary search
            elif nums[l] < nums[m]:
                if target < nums[m] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1


        return False