class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def link2list(ll):
    l = []
    n = ll
    while n is not None:
        l.append(n.val)
        n = n.next
    return l

def lst2link(lst):
    cur = dummy = ListNode(0)
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next



class Solution:
  def isPalindrome(self, head: ListNode) -> bool:
    def reverseList(head: ListNode) -> ListNode:
      prev = None
      curr = head

      while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

      return prev

    slow = head
    fast = head

    '''find the middle (slow)'''
    while fast and fast.next:

      slow = slow.next
      fast = fast.next.next

    ss = link2list(slow)
    for s in ss:
      print(s)

    '''reverse second half'''
    if fast:
      slow = slow.next

    slow = reverseList(slow)


    while slow:

      if slow.val != head.val:
        return False
      slow = slow.next
      head = head.next

    return True


if __name__ == '__main__':

    ls = [1, 2, 3, 4, 4, 3, 2, 1]

    ln = lst2link(ls)


    ss = Solution()
    res = ss.isPalindrome(ln)

    print(res)

