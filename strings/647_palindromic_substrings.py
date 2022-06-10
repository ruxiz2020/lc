class Solution:
    def countSubstrings(self, s):
        count = 0
        N = len(s)
        dp = [[False] * N for _ in range(N)]
        for l in range(1, N + 1):  # each possible length when the string length is l
            for start in range(N - l + 1):  # outer
                end = start + l - 1
                if l == 1 or (l == 2 and s[start] == s[end]) or \
                    (l >= 3 and s[start] == s[end] and dp[start + 1][end - 1]):  # dp

                    dp[start][end] = True
                    count += 1
        return count


class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res += self.countPali(s, i, i)
            res += self.countPali(s, i, i + 1)
        return res

    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res

        
