class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        lindex = {c: i for i, c in enumerate(S)}
        print(lindex)
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):

            j = max(j, lindex[c])
            if i == j:
                print(c, j, anchor)
                ans.append(j - anchor + 1)
                anchor = j + 1
        return ans



if __name__ == '__main__':

    s = "ababcbacadefegdehijhklij"

    ss = Solution()
    res = ss.partitionLabels(s)
    print(res)
