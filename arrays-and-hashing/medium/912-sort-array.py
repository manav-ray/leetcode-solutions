class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr, l, r, m):
            left, right = arr[l:m+1], arr[m+1:r+1]

            i, lp, rp = l, 0, 0

            while lp < len(left) and rp < len(right):
                if left[lp] <= right[rp]:
                    arr[i] = left[lp]
                    lp += 1
                else:
                    arr[i] = right[rp]
                    rp += 1
                
                i += 1
            
            while lp < len(left):
                arr[i] = left[lp]
                lp += 1
                i += 1

            while rp < len(right):
                arr[i] = right[rp]
                rp += 1
                i += 1    


        def merge_sort(arr, l, r):
            if l == r:
                return arr
            

            m = (l + r) // 2
            merge_sort(arr, l, m)
            merge_sort(arr, m+1, r)
            merge(arr, l, r, m)

            return arr
        
        return merge_sort(nums, 0, len(nums))