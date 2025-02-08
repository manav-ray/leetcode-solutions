"""

Using stack here since there are nested brackets. However, when we see a closing bracket,
we can calculate the "latest" substr until (a) we get to it's opening bracket and (b) we get
the count right before the bracket. We get the decoded substr from here then add to stack 
in case it's multiplied further up the call stack.

TC - Depends on input
SC - O(n)

"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != "]":
                stack.append(c)
            else:
                sub = ""
                while stack[-1] != "[":
                    sub = stack.pop() + sub
                
                stack.pop()

                cnt = ""
                while stack and stack[-1].isdigit():
                    cnt = stack.pop() + cnt
                
                cnt = int(cnt)

                stack.append(cnt * sub)
        

        return "".join(stack)