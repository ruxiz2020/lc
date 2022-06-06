import heapq

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
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        O(Nlogk)
Time complexity : O(N\log k)O(Nlogk) where \text{k}k is the number of linked lists.

The comparison cost will be reduced to O(\log k)O(logk) for every pop and insertion to priority queue. But finding the node with the smallest value just costs O(1)O(1) time.
There are NN nodes in the final linked list.
Space complexity :

O(n)O(n) Creating a new linked list costs O(n)O(n) space.
O(k)O(k) The code above present applies in-place method which cost O(1)O(1) space. And the priority queue (often implemented with heaps) costs O(k)O(k) space (it's far less than NN in most situations).
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





if __name__ == '__main__':

    lists = [[1,4,5],[1,3,4],[2,6]]

    arr_ll = []
    for l in lists:
        ll = lst2link(l)
        arr_ll.append(ll)


    ss = Solution()
    res = ss.mergeKLists(arr_ll)
    rr = link2list(res)

    print(list(rr))
