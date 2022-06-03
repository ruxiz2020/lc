import collections

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2) < len(s1): return False
        c = collections.Counter(s1)
        n = len(s1)
        l, r = 0, n - 1
        s = collections.Counter(s2[l : r])
        while r < len(s2):
            s[s2[r]] += 1
            if s == c:
                return True
            s[s2[l]] -= 1
            if s[s2[l]] == 0:
                del s[s2[l]]
            l += 1
            r += 1
        return False

if __name__ == '__main__':

    s1 = "ab"
    s2 = "eidbaooo"

    ss = Solution()
    res = ss.checkInclusion(s1, s2)
    print(res)
