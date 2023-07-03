"""
Approach
Define a new function checking whether the values are the same and applying recursion.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        


        def issame(subtree1,subtree2):

            if not subtree1 and subtree2: return False
            if not subtree2 and subtree1: return False
            if not subtree2 and not subtree1: return True

            return subtree1.val == subtree2.val and issame(subtree1.left,subtree2.left) and issame(subtree1.right, subtree2.right)

        return issame(p,q)