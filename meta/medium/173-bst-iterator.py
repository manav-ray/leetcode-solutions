"""

Your gut was right, learn to trust it
 - Just create a list of the inorder traversal -> 
   it's a lot easier to get elements in a list and check against its size

TC - O(n)
SC - O(n)

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.flat = []
        self.inorder(root)
        self.ptr = -1
    
    def inorder(self, root: Optional[TreeNode]):
        if not root:
            return
        
        self.inorder(root.left)
        self.flat.append(root.val)
        self.inorder(root.right)

    def next(self) -> int:
        self.ptr += 1
        return self.flat[self.ptr]

    def hasNext(self) -> bool:
        return self.ptr + 1 < len(self.flat)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()