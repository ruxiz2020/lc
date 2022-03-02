class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        res = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                res += customers[i]
                customers[i] = 0
        max_count = 0
        val = 0
        for i in range(len(customers)):
            if i < X:
                val += customers[i]
                continue
            max_count = max(val,max_count)
            val -= customers[i-X]
            val += customers[i]
        max_count = max(val, max_count)
        #print customers
        #print res
        return res + max_count
