class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1, l2 = len(word1), len(word2)
        dp1 = [i for i in range(l1 + 1)]
        dp2 = [0] * (l1 + 1)
        for i in range(1, l2 + 1):
            dp2[0] = i
            for j in range(1, l1 + 1):
                if word2[i - 1] == word1[j - 1]:# when current char are the same
                    dp2[j] = dp1[j - 1] # we care about previous substr
                else:
                    dp2[j] = min(dp1[j - 1], dp2[j - 1], dp1[j]) + 1 # add, delete, or replace
            dp1 = dp2[:]
        return dp1[-1]
