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


class Solution02(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        https://www.cnblogs.com/boring09/p/4231906.html
        单调递增stack
        O(n)
        """
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
            stack.append((start, h))

        # still some entries in stack
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea


if __name__ == '__main__':

    heights = [2,1,5,6,2,3]

    ss = Solution()
    res = ss.largestRectangleArea(heights)

    print(res)
