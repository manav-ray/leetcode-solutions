"""

Find the pivot point *
Run bs on left sorted array (0 -> pivot) -> If this returns != -1, return automatically
Run bs on right sorted array (pivot + 1 -> len(nums) - 2)

* Index is pivot if it's a peak element -> greater than i-1 and i+1
- Use bs to find pivot -> if index meets above conditions then set pivot
- If not, this is the logic to switch pointers -
    - if nums[m] >= nums[l], nums[l:m] is sorted, that means pivot is further down - set l to m + 1
    - If this is not the case, pivot is in left side of the array - set r to m - 1

Time complexity - O(logn)
Space complexity - O(1)

"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        pivot = 0

        while l <= r:
            m = (l + r) // 2
            if (
                m - 1 >= 0
                and m + 1 < len(nums)
                and nums[m - 1] <= nums[m]
                and nums[m + 1] <= nums[m]
            ):
                pivot = m
                break
            
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        
        def binarySearch(leftStart, rightEnd):
            print(leftStart, rightEnd)
            l, r = leftStart, rightEnd
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            
            return -1
            
        
        lRes = binarySearch(0, pivot)
        if lRes != -1:
            return lRes
        
        return binarySearch(pivot + 1, len(nums) - 1)