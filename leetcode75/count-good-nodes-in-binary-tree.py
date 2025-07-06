# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0

    def dfs(self, root: TreeNode, max_val: int):
        if root is None:
            return
        max_val = max(max_val, root.val)
        if root.val >= max_val:
            self.count += 1
        
        self.dfs(root.left, max_val)
        self.dfs(root.right, max_val)

    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root, -inf)
        return self.count
        
    
