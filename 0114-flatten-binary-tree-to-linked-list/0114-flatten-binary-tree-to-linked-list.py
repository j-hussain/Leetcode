# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if not root:
                return None

            l = dfs(root.left)
            r = dfs(root.right)

            if l:
                l.right = root.right
                root.right = root.left
                root.left = None

            final = r or l or root
            return final

        dfs(root)
