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


if __name__ == '__main__':

    s = "ABAB"
    k = 2

    ss = Solution()
    res = ss.characterReplacement(s, k)
    print(res)
