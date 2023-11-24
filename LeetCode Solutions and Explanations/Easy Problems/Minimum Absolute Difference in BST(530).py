"""
Intuition
My intuition for this problem is first extract all the values in BST to a list, then find the minimum absolute difference by sorting it.

Approach
get_vals() function recursively adds values to the lst until there is no node left.

Complexity
Time complexity:
O(n)
Space complexity:
O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        def get_vals(node,lst):
            if node:
                lst.append(node.val)

            else: return

            get_vals(node.left,lst)
            get_vals(node.right,lst)


            return lst


        lst = get_vals(root,[])
        lst.sort()
        dif = float('inf')
        for i in range(len(lst)-1):
            dif = min(dif, abs(lst[i]-lst[i+1]))

        return dif


            