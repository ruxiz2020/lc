class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        M, N = len(a), len(b)
        if M < N:
            a = "0" * (N - M) + a
        else:
            b = "0" * (M - N) + b
        stack1 = list(a)
        stack2 = list(b)
        res = ""
        carry = 0
        while stack1 and stack2:
            s1, s2 = stack1.pop(), stack2.pop()
            #print(s1, s2)
            cursum = int(s1) + int(s2) + carry
            if cursum >= 2:
                cursum %= 2
                carry = 1
            else:
                carry = 0
            res = str(cursum) + res
            print(res)
        if carry:
            res = "1" + res
        return res


ss = Solution()
a = "1010"; b = "1011"
print(a, b)
ss.addBinary(a, b)
