class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1
        
        stack = [(root1, root2)]
        
        while stack:
            node1, node2 = stack.pop()
            
            if not node1 or not node2:
                continue
            
            node1.val += node2.val
            
            if not node1.left:
                node1.left = node2.left
            else:
                stack.append((node1.left, node2.left))
            
            if not node1.right:
                node1.right = node2.right
            else:
                stack.append((node1.right, node2.right))
        
        return root1
