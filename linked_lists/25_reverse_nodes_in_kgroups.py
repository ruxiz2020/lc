# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        #迭代版，时间复杂度O(n)，空间复杂度O(1)
        # Need help
        if head == None: return head
        dummy = ListNode(0)
        dummy.next = head
        start = dummy  #  start =0.   Given this linked list: 1->2->3->4->5    #    For k = 2, you should return: 2->1->4->3->5
        while start.next:
            end = start                                # end = 0
            for i in range(k-1):
                end = end.next                         # end = 1
                if end.next == None: return dummy.next
            (start.next, start)=self.reverse(start.next, end.next)  #  (start.next=3, start=1)=self.reverse(start.next=1, end.next=2)
        return dummy.next

    def reverse(self, start, end):
        dummy = ListNode(0)
        dummy.next = start
        while dummy.next != end:
            tmp = start.next
            start.next = tmp.next
            tmp.next = dummy.next
            dummy.next = tmp
            #start.next, start.next.next, dummy.next = start.next.next, dummy.next, start.next
            # The above line is wrong! But WHY?
        return (end, start)
