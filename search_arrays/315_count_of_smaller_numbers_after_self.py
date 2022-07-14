class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        idxes = {}
        for k, v in enumerate(sorted(set(nums))):
            idxes[v] = k + 1
        iNums = [idxes[x] for x in nums]
        ft = FenwickTree(len(iNums))
        ans = [0] * len(nums)
        for i in range(len(iNums) - 1, -1, -1):
            ans[i] = ft.sum(iNums[i] - 1)
            ft.add(iNums[i], 1)
        return ans

class FenwickTree(object):
    def __init__(self, n):
        self.n = n
        self.sums = [0] * (n + 1)

    def add(self, x, val):
        while x <= self.n:
            self.sums[x] += val
            x += self.lowbit(x)

    def lowbit(self, x):
        return x & -x

    def sum(self, x):
        res = 0
        while x > 0:
            res += self.sums[x]
            x -= self.lowbit(x)
        return res



class Solution(object):
    def countSmaller(self, nums):
        def sort(enum):
            print(smaller)
            half = len(enum) // 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                m, n = len(left), len(right)
                i = j = 0
                while i < m or j < n:
                    if j == n or i < m and left[i][1] <= right[j][1]:
                        print(i, j)
                        enum[i+j] = left[i]
                        print('enum')
                        print(enum)
                        print('left')
                        print(left)
                        print('right')
                        print(right)
                        smaller[left[i][0]] += j
                        i += 1
                    else:
                        enum[i+j] = right[j]
                        j += 1
            return enum
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller


if __name__ == '__main__':

    nums = [5,2,6,1]

    ss = Solution()
    res = ss.countSmaller(nums)

    print(res)
