# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        answer = []
        
        if not root:
            return []

        def dfs(current, current_sum, path):
            if current is None:
                return

            path.append(current.val)
            current_sum += current.val

            if current.left is None and current.right is None:

                if current_sum == targetSum:
                    answer.append(list(path)) 
            else:
                dfs(current.left, current_sum, path)
                dfs(current.right, current_sum, path)

            path.pop()

        dfs(root, 0, [])
        
        return answer