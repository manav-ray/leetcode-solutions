"""

Your intuition for this is correct -> just have to go through the various edge cases.

Time complexity - O(n * m)
Space complexity - O(n * m)

"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == "0" or num2 == "0":
            return "0"

        num2_ptr = len(num2) - 1
        round_res = []

        trailing_zeros = 0
        while num2_ptr >= 0:
            carry = 0
            num1_ptr = len(num1) - 1
            curr_round_res = "0" * trailing_zeros

            while num1_ptr >= 0:
                curr_mul = int(num1[num1_ptr]) * int(num2[num2_ptr]) + carry
                res_digit = curr_mul % 10
                carry = curr_mul // 10

                curr_round_res = str(res_digit) + curr_round_res

                num1_ptr -= 1

            if carry == 0:
                round_res.append(curr_round_res)
            else:
                round_res.append(str(carry) + curr_round_res)

            trailing_zeros += 1
            num2_ptr -= 1

        res = self.add_all_numbers(round_res)

        return res
    

    def add_all_numbers(self, round_res):
        res = "0"
        for n in round_res:
            res = self.add_two_numbers(res, n)

        return res

    def add_two_numbers(self, num1, num2):
        res = ""
        i, j = len(num1) - 1, len(num2) - 1

        carry = 0

        while i >= 0 and j >= 0:
            curr_add = int(num1[i]) + int(num2[j]) + carry
            carry = curr_add // 10
            res_digit = curr_add % 10

            res = str(res_digit) + res

            i -= 1
            j -= 1

        while i >= 0:
            digit = int(num1[i]) + carry
            carry = digit // 10
            res = str(digit % 10) + res
            i -= 1
        
        while j >= 0:
            digit = int(num2[j]) + carry
            carry = digit // 10
            res = str(digit % 10) + res
            j -= 1
        
        res = str(carry) + res if carry != 0 else res
        return res