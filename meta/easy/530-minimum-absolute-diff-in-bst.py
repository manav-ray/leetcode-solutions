"""

Since bst, inorder traversal will give nodes in sorted order. Smallest difference would be in neighboring nodes in this list.

Time complexity - O(n)
Space complexity - O(n)

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        inorder_list = []

        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            inorder_list.append(root.val)
            inorder(root.right)

        
        inorder(root)

        res = 100000

        for i in range(len(inorder_list) - 1):
            res = min(res, abs(inorder_list[i] - inorder_list[i+1]))
        
        return res