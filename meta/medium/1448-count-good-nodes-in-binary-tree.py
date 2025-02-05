"""

This question tests your knowledge about differentiating between different tree traversals.
Since we're doing calculations pertaining to the root of the tree (and each subtree), we need to process the root
of the tree first, hence we go for a pre order traversal.

 - For each recursive call, we first increment res if curr root val is larger than the currmax.
 - Then, we update currmax to the maximum value we've seen so far (We only need to keep track of the currMax
   since that's all we're calculating good nodes against)

TC - O(n)
SC - O(h) -> height (recursive call stack)


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0

        res = 0
        
        def countGoodNodesInPreOrder(root, currMax):
            nonlocal res
            
            if not root:
                return
            
            if root.val >= currMax:
                res += 1

            maxVal = max(currMax, root.val)
            countGoodNodesInPreOrder(root.left, maxVal)
            countGoodNodesInPreOrder(root.right, maxVal)
        
        countGoodNodesInPreOrder(root, root.val)

        return res