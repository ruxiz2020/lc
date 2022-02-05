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

def link2list(ll):
    l = []
    n = ll
    while n is not None:
        l.append(n.val)
        n = n.next
    return l


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


if __name__ == '__main__':

    arr = [1,2,3,4,5]
    n = 2

    head = lst2link(arr)

    ss = Solution()
    res = ss.removeNthFromEnd(head, n)

    rr = link2list(res)

    print(list(rr))
