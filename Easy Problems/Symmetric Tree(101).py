"""
Approach
To check the symmetric condition, we can define a function (issym in my code) checking whether the values of left and right node are the same and apply this procedure recursively until it reaches the leaf nodes.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root: return False #base case

        def issym(subtree1,subtree2):

            if subtree1 and not subtree2: return False
            if subtree2 and not subtree1: return False
            if not subtree1 and not subtree2: return True


            
            return subtree1.val == subtree2.val and issym(subtree1.right,subtree2.left) and issym(subtree1.left,subtree2.right)


        return issym(root.left, root.right) 