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
        :rtype: int
        """
        
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1

        def dfs(node, curr_sum):
            if not node:
                return 0

            curr_sum += node.val
            count = prefix_counts[curr_sum - targetSum]

            prefix_counts[curr_sum] += 1
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)
            prefix_counts[curr_sum] -= 1

            return count

        return dfs(root, 0)