# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = []

        def dfs(node, index=1):
            if not node:
                return

            queue.append(index)
            dfs(node.left, 2*index)
            dfs(node.right, 2*index+1)

        dfs(root)
        return max(queue) == len(queue)