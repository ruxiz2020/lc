class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        pos = collections.defaultdict(int)
        for i in range(len(S)):
            pos[S[i]] = i
        res = sorted(T, key = lambda x : pos[x])
        return "".join(res)
