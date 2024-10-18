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
            
            left_sum = max(dfs(node.left), 0)
            right_sum = max(dfs(node.right), 0)
            
            current_path_sum = node.val + left_sum + right_sum
            self.max_sum = max(self.max_sum, current_path_sum)
            
            return node.val + max(left_sum, right_sum)
        
        self.max_sum = float('-inf')
        dfs(root)
        return self.max_sum
