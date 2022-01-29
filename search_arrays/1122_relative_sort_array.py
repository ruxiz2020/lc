class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        res = []
        c = collections.Counter(arr1)
        for x in arr2:
            res += [x] * c.pop(x)
        return res + sorted(c.elements())
