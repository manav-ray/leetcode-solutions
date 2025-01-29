"""

 - Symbol list contains generic symbols + special cases (4, 9, etc)
 - Since we convert from highest to lowest, start from highest roman value.
 - For every symbol in the list, check if it goes into the remaining num.
 - The number of times it goes into the number is the number of times the symbol needs to show up
 - Mod divide number by symbol value after doing this since we have already checked the number of times it goes into number.

Time complexity - O(1)
Space complexity - O(1)

"""


class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""

        symList = [
            ["I", 1],
            ["IV", 4],
            ["V", 5],
            ["IX", 9],
            ["X", 10],
            ["XL", 40],
            ["L", 50],
            ["XC", 90],
            ["C", 100],
            ["CD", 400],
            ["D", 500],
            ["CM", 900],
            ["M", 1000],
        ]

        for sym, val in reversed(symList):
            if num // val:
                count = num // val
                res += count * sym
                num = num % val

        return res
