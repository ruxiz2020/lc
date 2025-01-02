import heapq

from typing import List


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



class Solution01(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        O(Nlogk)
        O(n)
     """
        heap = []
        root = res = ListNode(None)
        for l in lists:
            while l:
                heapq.heappush(heap, l.val) # O(log n)
                l = l.next
        print(heap)
        while heap:
            res.next = ListNode(heapq.heappop(heap)) # O(log n)
            res = res.next
        return root.next



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution02:
    '''nlog(k)'''
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2): # O(log K)
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2)) # O(N)
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next



if __name__ == '__main__':

    lists = [[1,4,5],[1,3,4],[2,6]]

    arr_ll = []
    for l in lists:
        ll = lst2link(l)
        arr_ll.append(ll)


    ss = Solution01()
    res = ss.mergeKLists(arr_ll)
    rr = link2list(res)

    print(list(rr))
