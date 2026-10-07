from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root:
            q = deque([root])
            while q:
                level_size = len(q)
                res.append(q[-1].val)
                for i in range(level_size):
                    n = q.popleft()
                    if n.left:
                        q.append(n.left)
                    if n.right:
                        q.append(n.right)
        return res

