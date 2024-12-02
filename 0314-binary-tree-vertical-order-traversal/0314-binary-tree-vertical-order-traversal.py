# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        table = defaultdict(list)
        if not root:
            return []
        queue = deque([(root, 0)])
        mincol, maxcol = 0, 0
        while queue:
            node, column = queue.popleft()
            if node is not None:
                table[column].append(node.val)
                mincol = min(mincol, column)
                maxcol = max(maxcol, column)
                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))
        return [table[x] for x in range(mincol, maxcol + 1)]