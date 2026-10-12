# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        if head == None:
          return None

        less_nodes = ListNode()
        more_nodes = ListNode()
        pointer_less = less_nodes
        pointer_more = more_nodes
        current = head

        while current is not None:
          if current.val >= x:
              pointer_more.next = current
              pointer_more = pointer_more.next
          
          else:
              pointer_less.next = current
              pointer_less = pointer_less.next

          current = current.next

        pointer_more.next = None

        pointer_less.next = more_nodes.next

        return less_nodes.next