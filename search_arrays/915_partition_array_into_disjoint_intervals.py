class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        时间复杂度是O(N)，空间复杂度是O(1)
        """
        disjoint = 0
        v = A[0]
        max_so_far = v
        for i in range(len(A)):
            max_so_far = max(max_so_far, A[i])
            if A[i] < v:
                v = max_so_far
                disjoint = i
        return disjoint + 1
