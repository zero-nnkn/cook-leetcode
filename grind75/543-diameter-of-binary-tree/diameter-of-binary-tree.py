# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def len_and_diameter(root):
            if root is None:
                return 0, 0
            left_len, left_diameter = len_and_diameter(root.left)
            right_len, right_diameter = len_and_diameter(root.right)
            root_len = max(left_len, right_len) + 1
            root_diameter = max(left_len + right_len, left_diameter, right_diameter)
            return root_len, root_diameter

        root_len, root_diameter = len_and_diameter(root)
        return root_diameter
        