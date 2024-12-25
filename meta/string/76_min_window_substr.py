class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        O( S + T)
        O(U) u: number of unique characters in t
        """
        if t == "": return ""
        countT = {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = '', float('inf')
        l, r = 0, 0

        for r in range(len(s)):  # enlarge the window to the right
            if s[r] in countT:
                countT[s[r]] -= 1
                if countT[s[r]] == 0:
                    have += 1

            # move left pointer
            while (l <= r and have == need):
                print(l, r, res)
                Len = r + 1 - l
                if Len < resLen:
                    res = s[l:r + 1]
                    resLen = Len

                if s[l] in countT:
                    countT[s[l]] += 1
                    if countT[s[l]] == 1:
                        have -= 1

                l += 1

        return res


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"

    ss = Solution()
    res = ss.minWindow(s, t)
    print(res)
