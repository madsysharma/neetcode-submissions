# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            
            is_good = 1 if node.val >= max_val else 0
            new_max = max(max_val, node.val)
            return is_good + dfs(node.left, new_max) + dfs(node.right, new_max)

        if root:
            return dfs(root, root.val)
        else:
            return 0
        