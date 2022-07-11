from collections import Counter


class Solution:
    '''O(n)'''
    def characterReplacement(self, s, k):
        ans = 0
        maxCount = 0
        count = Counter()

        l = 0
        for r, c in enumerate(s):
            count[c] += 1
            maxCount = max(maxCount, count[c])
            print(maxCount)
            while maxCount + k < r - l + 1:
                count[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)

        return ans




class Solution:
    '''O(26n) ---> O(n) since maxf is only increasing'''
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])  # only increasing, since when this number becomes smaller result is not changing
            print(maxf)

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res

if __name__ == '__main__':

    s = "AABABBACBB"
    k = 2

    ss = Solution()
    res = ss.characterReplacement(s, k)
    print(res)
