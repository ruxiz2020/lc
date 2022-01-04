class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return not re.match(".*A.*A.*", s) and not re.match(".*LLL.*", s)


class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        N = len(s)
        s = s + "P"
        countA = 0
        countL = 0
        for i in range(N):
            if s[i] == "A":
                countA += 1
            if countA > 1:
                return False
            if s[i] == "L":
                countL += 1
                if countL >= 3:
                    return False
            else:
                countL = 0
        return True
