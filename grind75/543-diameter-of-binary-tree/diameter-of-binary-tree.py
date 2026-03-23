# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # def height_and_diameter(root):
        #     if root is None:
        #         return 0, 0
        #     left_height, left_diameter = height_and_diameter(root.left)
        #     right_height, right_diameter = height_and_diameter(root.right)
        #     root_height = max(left_height, right_height) + 1
        #     root_diameter = max(left_height + right_height, left_diameter, right_diameter)
        #     return root_height, root_diameter

        # root_height, root_diameter = height_and_diameter(root)
        # return root_diameter

        self.diameter = 0
        
        def height(root):
            if root is None:
                return 0
            left_height = height(root.left)
            right_height = height(root.right)
            self.diameter = max(self.diameter, left_height + right_height)
            return max(left_height, right_height) + 1
        
        height(root)
        
        return self.diameter
        