"""

Time Complexity - O(max(a, b))
Space Complexity - O(max(a, b))

"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""

        a_ptr, b_ptr = len(a) - 1, len(b) - 1
        carry = 0

        while a_ptr >= 0 and b_ptr >= 0:
            curr_sum = carry + int(a[a_ptr]) + int(b[b_ptr])
            carry = curr_sum // 2
            new_digit = curr_sum % 2 


            res += str(new_digit)
            a_ptr -= 1
            b_ptr -= 1
        
        while a_ptr >= 0:
            curr_sum = carry + int(a[a_ptr])
            carry = curr_sum // 2
            new_digit = curr_sum % 2 


            res += str(new_digit)
            a_ptr -= 1

        while b_ptr >= 0:
            curr_sum = carry + int(b[b_ptr])
            carry = curr_sum // 2
            new_digit = curr_sum % 2 


            res += str(new_digit)
            b_ptr -= 1

        if carry != 0:
            res += str(carry)

        return res[::-1]