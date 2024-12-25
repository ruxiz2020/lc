class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        O(M * N)
        O(1)
        """
        if not strs: return ""
        pre = min(strs, key = len)
        print(pre)
        for i, c in enumerate(pre):
            for word in strs:
                if word[i] != c:
                    return pre[:i]
        return pre

if __name__ == '__main__':

    strs = ["flower","flow","flight"]

    ss = Solution()
    res = ss.longestCommonPrefix(strs)
    print(res)
