# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        root = ListNode(0)
        root.next = head
        fast, slow, pre = root, root, root
        while n - 1:
            fast = fast.next
            n -= 1
        while fast.next:
            fast = fast.next
            pre = slow
            slow = slow.next
        pre.next = slow.next
        return root.next
