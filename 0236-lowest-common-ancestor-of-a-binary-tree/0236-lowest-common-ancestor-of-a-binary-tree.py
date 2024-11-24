# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None
        def recurse(node):
            nonlocal res
            if not node:
                return False
                
            l = recurse(node.left)
            r = recurse(node.right)

            flag = (node == q) or (node == p)

            if l + flag + r >= 2:
                res = node

            return flag or l or r

        recurse(root)
        return res