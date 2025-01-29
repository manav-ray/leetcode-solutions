"""

Stack is the correct approach for this one
If we encounter a "-" or number, that means we are getting a node value. In this case, parse the value and add that node to the stack
If we encounter a ")", that means we are done with the latest node, pop it from the stack and add it to the most recent parent (left first, then right if not avail)
Note: There is no special case for "(" - This is the delimeter used to start parsing a number from the next index. This could be a part of step one but not required.

Time Complexity - O(n)
Space complexity - O(n)

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None
        
        i = 0
        stack = []
        while i < len(s):
            if s[i].isdigit() or s[i] == "-":
                val, index = self.getNumber(s, i)
                i = index
                i -= 1

                stack.append(TreeNode(val))
            elif s[i] == ")":
                nodeToAdd = stack.pop()
                if not stack[-1].left:
                    stack[-1].left = nodeToAdd
                else:
                    stack[-1].right = nodeToAdd
                
            i += 1
        
        return stack[-1]


    def getNumber(self, s, idx):
        res = 0
        i = idx
        sign = 1
        if s[i] == "-":
            sign = -1
            i += 1

        while i < len(s) and s[i].isdigit():
            res = (res * 10) + int(s[i])
            i += 1
        
        return res * sign, i