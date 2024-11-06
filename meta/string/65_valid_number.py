class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip().lower()
        if not s: return False
        if s[0] == '+' or s[0] == '-': s = s[1:]
        try:
            pointindex = s.index('.')
        except:
            pointindex = -1
        try:
            eindex = s.index('e')
        except:
            eindex = -1
        if eindex != -1:
            if eindex == len(s)-1: return False
            epart = s[eindex+1:]
            s = s[:eindex]
            if epart[0] == '+' or epart[0] == '-':
                epart = epart[1:]
                if not epart: return False
            for i in epart:
                if not i.isdigit(): return False
        if s == '.' or not s: return False
        s = s[:pointindex] + s[pointindex+1:]
        try:
            s.index('.')
            return False
        except:
            for j in s:
                if not j.isdigit(): return False
            return True


"""
For example, all the following are valid numbers: "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", while the following are not valid numbers: "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53".

"""

num = "-90E3"

ss = Solution()
res = ss.isNumber(num)
print(res)
