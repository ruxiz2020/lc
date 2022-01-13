class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        w1 = [i for i in range(len(words)) if words[i]==word1]
        w2 = [i for i in range(len(words)) if words[i]==word2]
        return min([abs(i-j) for i in w1 for j in w2])
