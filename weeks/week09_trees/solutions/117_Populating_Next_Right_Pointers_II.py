"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        current = root

        while current:
          dummy = Node(0)
          tail = dummy

          while current:

            if current.left:
              tail.next = current.left
              tail = tail.next
            if current.right:
              tail.next = current.right
              tail = tail.next

            current = current.next

          current = dummy.next

        return root