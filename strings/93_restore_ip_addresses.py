class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) > 12:
            return []
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        #print(s, path, res)
        if len(s) > (4 - len(path)) * 3:
            return
        if not s and len(path) == 4:
            res.append('.'.join(path))
            return
        for i in range(1, 4):
            if i > len(s):
                print(s, i)
                continue
            number = int(s[:i])
            if str(number) == s[:i] and number <= 255:
                self.dfs(s[i:], path + [s[:i]], res)



if __name__ == '__main__':

    s = "25525511135"

    ss = Solution()
    res = ss.restoreIpAddresses(s)
    print(res)
