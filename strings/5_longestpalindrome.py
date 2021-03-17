class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        O(n^2)
        """
        if not s:
            return ''
        n = len(s)
        res = ''
        for i in range(n):
            single = self.get_max_substr(s, i, i)
            double = self.get_max_substr(s, i, i+1)
            bigger = None
            if len(single) > len(double):
                bigger = single
            else:
                bigger = double
            if len(bigger) > len(res):
                res = bigger
        return res

    def get_max_substr(self, strs, l, r):
        res = ''
        n = len(strs)
        while l >= 0 and r < n and strs[l] == strs[r]:
            if len(res) < len(strs[l:r+1]):
                res = strs[l:r+1]
            l -= 1
            r += 1
        return res
