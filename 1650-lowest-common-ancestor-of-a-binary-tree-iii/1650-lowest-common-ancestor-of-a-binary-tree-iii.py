"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        pc, qc = 0, 0
        pog, qog = p, q
        while p:
            p = p.parent
            pc += 1
        while q:
            q = q.parent
            qc += 1
        p, q = pog,  qog
        while pc > qc:
            p = p.parent
            pc -= 1
        while qc > pc:
            q = q.parent
            qc -= 1
        
        while p and q:
            if p == q:
                return p
                
            p = p.parent
            q = q.parent

        return None