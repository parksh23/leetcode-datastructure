# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        first = head
        second = head
        if first == None:
            return False
        while first.next is not None:
            first = first.next
            if first.next == second.next:
                return True

            first = first.next
            if first == None:
                return False
            second = second.next
            if first.next == second.next:
                return True

        return False