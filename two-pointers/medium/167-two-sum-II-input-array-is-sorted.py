class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        
        while start < end:
            
            currSum = numbers[start] + numbers[end]
            
            if currSum == target:
                return [start+1, end+1]
            elif currSum < target:
                start += 1
            else:
                end -= 1
        
        return [-1, -1]