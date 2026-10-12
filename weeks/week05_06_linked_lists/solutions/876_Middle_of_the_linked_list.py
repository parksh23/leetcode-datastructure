# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        fast = head
        slow = head

        while fast is not None:
          fast = fast.next
          if fast == None:
            break
          
          slow = slow.next
          fast = fast.next

        return slow