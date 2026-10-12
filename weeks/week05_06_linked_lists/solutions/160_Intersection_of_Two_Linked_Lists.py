# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pointer_A = headA
        pointer_B = headB

        while pointer_A != pointer_B:
          pointer_A = pointer_A.next if pointer_A else headB
          pointer_B = pointer_B.next if pointer_B else headA

        return pointer_A