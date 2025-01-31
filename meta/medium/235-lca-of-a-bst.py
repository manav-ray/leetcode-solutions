"""

Recursive approach
Time complexity - O(logn) 
Space complexity - O(h) -> height of bst

"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        

        return root
    

"""

Iterative approach
Time complexity - O(logn)
Space complexity - O(1)

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
        
            if p.val > root.val and q.val > root.val:
                root = root.right
            
            elif p.val < root.val and q.val < root.val:
                root = root.left
            
            else:
                return root
        

        return None