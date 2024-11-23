# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def lst2link(lst):
    cur = dummy = ListNode(0)
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        beforeHead = ListNode(0)
        afterHead = ListNode(0)
        before = beforeHead
        after = afterHead

        while head:
            if head.val < x:
                before.next = head
                before = head
            else:
                after.next = head
                after = head
            head = head.next

        after.next = None
        before.next = afterHead.next

        return beforeHead.next


lst = [1,4,3,2,5,2]; x = 3 # res [1,2,2,4,3,5]
head = lst2link(lst)

res = Solution().partition(head, x)

current = res
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")
