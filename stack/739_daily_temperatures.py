class Solution:
    def dailyTemperatures(self, T):
        '''Monotonic decreasing stack'''
        if not T:
            return []
        res = [0] * len(T)
        stack = []
        for index, val in enumerate(T):
            while stack and stack[-1][0] < val:
                stack_top_index = stack.pop()[1]
                count = index - stack_top_index
                res[stack_top_index] = count
            stack.append((val, index))
        return res


if __name__ == '__main__':

    temperatures = [73,74,75,71,69,72,76,73]

    ss = Solution()
    res = ss.dailyTemperatures(temperatures)

    print(res)
