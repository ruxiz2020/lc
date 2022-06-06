class Solution:
    def findRepeatedDnaSequences(self, s):
        seen = set()
        res = set()
        for i in range(len(s) - 9):
            tmp=s[i: i + 10]
            if tmp in seen:
                res.add(tmp)
            else:
                seen.add(tmp)
        return res

if __name__ == '__main__':

    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

    ss = Solution()
    res = ss.findRepeatedDnaSequences(s)
    print(res)
