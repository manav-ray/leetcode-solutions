"""

Time complexity - O(n)
Space complexity - O(1)

"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        carry = 0

        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                add = (digits[i] + 1) % 10
                carry = (digits[i] + 1) // 10
            
            else:
                add = (digits[i] + carry) % 10
                carry = (digits[i] + carry) // 10
            
            res.append(add)
        
        if carry != 0:
            res.append(carry)
        
        return res[::-1]