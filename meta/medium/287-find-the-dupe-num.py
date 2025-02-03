"""

Negative marking ->
 An array of size n + 1 contains only positive integers from [1, n]
 Since the len of nums matches the elements in nums, the elements of nums
 would only contain valid indices that lie in nums. Because of this, we can use
 negative marking to see if an element has already been visited:
  - For each elem in nums, take the abs value of it (since it's possible we negative marked)
  - Check if the element at nums[abs(n)] is negative, that means we have already come to this element
    - How? We only visit elements from iteration or from the logic above. From the logic above, an element
      can only be marked negative if it's index was referenced by another element.
    - Due to this, it means abs(n) is a duplicate.

- THINK OF THIS AS FINDING DUPLICATE POINTER. FOR EACH ITERATION, WE ARE GOING TO WHATEVER ELEMENT POINTED
  BY THE CURRENT ELEMENT. TO AVOID USING EXTRA SPACE, WE MARK THE VISITED ELEMENT AS NEGATIVE. SINCE THERE
  IS A DUPE ELEMENT IN THE INPUT AND SINCE WE'RE LOOKING AT THE ELEMENTS AS POINTERS, THERE WILL BE A DUPLICATE
  POINTER IN THE LIST. THAT MEANS THERE WILL BE A TIME WHEN THE SAME ELEMENT WILL BE REFERENCED TWICE (WHICH WE
  CHECK BY LOOKING FOR NEGATIVITY). WHEN THIS HAPPENS, IT MEANS THE POINTER WE USED TO GET TO THIS ELEMENT IS
  DUPLICATE, HENCE WE RETURN IT.

Time complexity - O(n)
Space complexity - O(1)

"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for n in nums:
            nxt = nums[abs(n)]
            if nxt < 0:
                return abs(n)
            
            nums[abs(n)] *= -1
        
        return -1