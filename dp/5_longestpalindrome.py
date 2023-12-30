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
            double = self.get_max_substr(s, i, i + 1)
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
            if len(res) < len(strs[l:r + 1]):
                res = strs[l:r + 1]
            l -= 1
            r += 1
        return res


class Solution(object):
    def longestPalindrome(self, s):
        longest = '' if not s else s[0]
        max_len = 1
        size = len(s)
        dp = [[False] * size for _ in range(size)]
        for start in range(size - 1, -1, -1):
            dp[start][start] = True
            for end in range(start + 1, size):
                if s[start] == s[end]:
                    if end - start == 1 or dp[start + 1][end - 1]:
                        dp[start][end] = True
                        if max_len < end - start + 1:
                            max_len = end - start + 1
                            longest = s[start: end + 1]
        return longest


class Solution(object):
    def longestPalindrome(self, s):
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd number
            l, r = i, i
            while l >= 0 and r < len(s) and s[1] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even number
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[1] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res
