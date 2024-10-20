from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)
            
            path_sum = node.val + left_max + right_max
            self.global_max = max(self.global_max, path_sum)
            
            return node.val + max(left_max, right_max)
        
        self.global_max = float('-inf')
        dfs(root)
        return self.global_max
