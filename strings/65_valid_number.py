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
