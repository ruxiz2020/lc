class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        val = [0] * 2001
        for i in arr1:
            val[i] += 1
        for i in arr2:
            val[i] += 1
        for i in arr3:
            val[i] += 1
        res = []
        for i,v in enumerate(val):
            if v == 3:
                res.append(i)
        return res
