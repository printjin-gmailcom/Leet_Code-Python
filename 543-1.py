from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            self.diameter = max(self.diameter, left_height + right_height)
            return 1 + max(left_height, right_height)
        
        self.diameter = 0
        height(root)
        return self.diameter
