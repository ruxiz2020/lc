class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap = {}
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = t[i]
            elif hashmap[s[i]] != t[i]:
                return False
        mapval = [hashmap[k] for k in hashmap]
        return len(mapval) == len(set(mapval))


if __name__ == '__main__':

    s = "egg"; t = "add"
    ss = Solution()
    res = ss.isIsomorphic(s)
    print(res)
