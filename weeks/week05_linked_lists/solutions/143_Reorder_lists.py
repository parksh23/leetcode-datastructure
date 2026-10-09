# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        result = head
        fast = head
        slow = head

        while fast:
            fast = fast.next
            if not fast:
                break
            slow = slow.next
            fast = fast.next

        prev = None
        temp = slow.next
        slow.next = None

        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node

        while prev:
            temp1 = head.next
            temp2 = prev.next
            head.next = prev
            prev.next = temp1
            head = temp1
            prev = temp2