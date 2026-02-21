# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(
        self, 
        root: 'TreeNode', 
        p: 'TreeNode', 
        q: 'TreeNode'
    ) -> 'TreeNode':
        def dfs(root, small, big):
            if root.val == small.val:
                return small
            elif root.val == big.val:
                return big
            elif small.val < root.val < big.val:
                return root
            elif root.val < small.val:
                return dfs(root.right, small, big)
            elif root.val > big.val:
                return dfs(root.left, small, big)
        
        if p.val < q.val:
            return dfs(root, p, q)
        else:
            return dfs(root, q, p)


        