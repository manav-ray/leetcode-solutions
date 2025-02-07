"""

First observation -> We can't have k > len(s) because we can't make k non-empty substrings
Next -> For a string to be a palindrome, there can be at most 1 odd count character (the middle character)
 - So if we're making k palindromes, there can be at most k odd count characters.

TC - O(n)
SC - O(1)

"""


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        
        counts = Counter(s)

        odds = 0
        for cnt in counts.values():
            odds += cnt % 2

        return odds <= k 