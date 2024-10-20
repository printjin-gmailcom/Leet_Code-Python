from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0
            
            left_sum = max(dfs(node.left), 0)  # Only consider positive sums
            right_sum = max(dfs(node.right), 0)
            
            max_sum = max(max_sum, node.val + left_sum + right_sum)
            
            return node.val + max(left_sum, right_sum)
        
        max_sum = float('-inf')
        dfs(root)
        return max_sum
