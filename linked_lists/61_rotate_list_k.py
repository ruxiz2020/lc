# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0:
            return head
        if head == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        count = 0
        while p.next:
            p = p.next
            count += 1
        p.next = dummy.next
        step = count - ( k % count )
        for i in range(0, step):
            p = p.next
        head = p.next
        p.next = None
        return head
