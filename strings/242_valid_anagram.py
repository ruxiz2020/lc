class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        O(s+t)
        """
        if len(s) != len(t):
            return False

        alpha = {}
        beta = {}
        for c in s:
            alpha[c] = alpha.get(c, 0) + 1
        for c in t:
            beta[c] = beta.get(c, 0) + 1
        return alpha == beta


if __name__ == '__main__':

    s = "anagram"
    t = "nagaram"

    ss = Solution()
    res = ss.isAnagram(s, t)
    print(res)
