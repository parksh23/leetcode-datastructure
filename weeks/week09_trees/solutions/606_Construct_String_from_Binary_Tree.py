# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: str
        """
        if not root:
          return ""

        result = str(root.val)

        if root.left or root.right:
          result += f"({self.tree2str(root.left)})"

        if root.right:
          result += f"({self.tree2str(root.right)})"

        return result