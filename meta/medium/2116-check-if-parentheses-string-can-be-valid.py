"""

Have to go both forward and backwards direction
 - They check the same thing except for one minor change, closing vs opening parentheses.

Logic for a direction - 
 - If there are an odd number of parentheses, auto return False as we don't have even pairs
 - Keep track of open parentheses, as well as unlocked
 - If we encounter an unlocked spot, increment unlocked count (this can be open or close, aka wildcard)
 - If we encounter open increment open count
 - If we encounter close, check if there is associated open
 - If not, check if we have unlocked to use here
 - If not, return false

Check exact same thing but opposite for other direction
 - At the very end, if we execute the full thing without returning False, we have a can be valid string -> return True

Time complexity - O(n)
Space complexity - O(1)

"""


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        openP = 0
        unlocked = 0

        for i, p in enumerate(s):
            if locked[i] == "0":
                unlocked += 1
            elif p == "(":
                openP += 1
            elif p ==")":
                if openP > 0:
                    openP -= 1
                elif unlocked > 0:
                    unlocked -= 1
                else:
                    return False

        closeP = 0
        unlocked = 0

        for i in range(len(s) - 1, -1, -1):
            p = s[i]
            if locked[i] == "0":
                unlocked += 1
            elif p == ")":
                closeP += 1
            elif p =="(":
                if closeP > 0:
                    closeP -= 1
                elif unlocked > 0:
                    unlocked -= 1
                else:
                    return False
        
        return True