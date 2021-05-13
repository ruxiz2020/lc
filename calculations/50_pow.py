class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if 0 == n:
            return 1
        elif n < 0:
            return 1.0 / self.myPow(x, -n)
        else:
            half = self.myPow(x, n // 2) # or n >> 1
            if 0 == n % 2:
                return half * half
            else:
                return x * half * half


x = 2.00000; n = 10
print("input: x = 2.00000, n = 10")

ss = Solution()
res = ss.myPow(x, n)
print("res: " + str(res))
