# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        current = root

        def dfs(current):
          if not current:
            return 0

          left = dfs(current.left)
          right = dfs(current.right)

          return max(left, right) + 1

        return dfs(current)
          