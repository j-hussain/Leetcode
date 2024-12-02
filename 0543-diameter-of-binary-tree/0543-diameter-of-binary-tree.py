# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def longestpath(node):
            nonlocal diameter
            if node is None:
                return 0
            l=longestpath(node.left)
            r=longestpath(node.right)
            diameter = max(diameter, l+r)

            return max(l,r) + 1

        longestpath(root)
        return diameter