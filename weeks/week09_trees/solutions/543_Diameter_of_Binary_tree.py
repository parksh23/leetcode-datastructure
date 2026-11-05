# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.result = 0

        def dfs(current):
          if current is None:
            return 0

          left_depth = dfs(current.left)
          right_depth = dfs(current.right)

          self.result = max(self.result, left_depth + right_depth)

          return max(left_depth, right_depth) + 1

        dfs(root)
        return self.result