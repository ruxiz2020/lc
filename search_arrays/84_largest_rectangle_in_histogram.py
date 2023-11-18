class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        https://www.cnblogs.com/boring09/p/4231906.html
        单调递增stack
        O(n)
        """
        stack = list()
        res = 0
        heights.append(0)
        N = len(heights)
        for i in range(N):
            print(stack)
            print(res)
            if not stack or heights[i] > heights[stack[-1]]:
                stack.append(i)
            else:
                while stack and heights[i] <= heights[stack[-1]]:
                    h = heights[stack[-1]] # compute the max area from last bar
                    stack.pop()
                    w = i if not stack else i - stack[-1] - 1
                    res = max(res, h * w)
                stack.append(i)
        return res


if __name__ == '__main__':

    heights = [2,1,5,6,2,3]

    ss = Solution()
    res = ss.largestRectangleArea(heights)

    print(res)
