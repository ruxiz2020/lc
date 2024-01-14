class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        lap = 0
        depth_len = {0: 0}
        for line in input.splitlines():
            name = line.lstrip('\t')
            #print(name)
            # 前面有几个'\t', depth就是几, 因为'\t'的长度为1
            depth = len(line) - len(name)
            #print(depth)
            if '.' in name:
                lap = max(lap, depth_len[depth]+len(name))
            else:
                # 加1是为了加上一个path分隔符'/'的长度
                depth_len[depth+1] = depth_len[depth] + 1 + len(name)
                print(depth_len)
        return lap

if __name__ == '__main__':

    input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

    ss = Solution()
    res = ss.lengthLongestPath(input)
    print(res)
