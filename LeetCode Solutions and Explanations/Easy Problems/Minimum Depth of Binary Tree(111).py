"""
Intuition
To find the minimum depth we need to find the leaf node and return the depth + 1.

-> If left node is none then return depth_right_node + 1
-> If rigth node is none then return depth_left_node + 1

We need a recursive function like many binary tree problems to find the leaf nodes

Approach
find_depth function calculates left and right depth in each iteration. left_depth is responsible from left side of the branches and right_depth is responsible from the rest.

** A reminder for me: In first look, it seems like left depth only considers left childs, but if you look closely the recursion gives me an opportunity to consider right nodes also.

Add the necessary conditions which I've descirbed above.

And finally, return minimum of left_depth and right_depth + 1
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        def find_depth(node):
            if not node: return 0
            else:
                left_depth = find_depth(node.left)
                right_depth = find_depth(node.right)


                if not left_depth: return right_depth+1
                elif not right_depth: return left_depth+1
                
                else:
                    return min(right_depth,left_depth)+1


        return find_depth(root)
