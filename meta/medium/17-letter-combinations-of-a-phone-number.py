"""

Classic backtracking:
 - Combo length will always equal len of digits passed in
 - To add a letter to the combo, we need backtracking -> 
    - Loop through letters associated with digit, and call backtrack by adding it to combo, then remove it from combo 
      so that it isn't included in next backtrack call.


Time complexity - O(4^n) -> At most 4 decisions per number in digits
Space complexity - O(n) -> Recursive call stack

"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits == "":
            return []

        res = []

        combos = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(curr_combo):
            if len(curr_combo) == len(digits):
                res.append(curr_combo)
                return
            
            letter_idx = len(curr_combo)
            letter_mapping = combos[digits[letter_idx]]

            for c in letter_mapping:
                backtrack(curr_combo + c)

        backtrack("")

        return res