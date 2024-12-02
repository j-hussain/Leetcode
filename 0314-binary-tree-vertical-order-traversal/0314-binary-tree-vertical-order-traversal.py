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
            node, col = queue.popleft()
            if node is not None:
                table[col].append(node.val)
                mincol = min(mincol, col)
                maxcol = max(maxcol, col)
                queue.append((node.left, col - 1))
                queue.append((node.right, col + 1))

        return [table[x] for x in range(mincol, maxcol + 1)]