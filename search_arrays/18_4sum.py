class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]

        """
        N = len(nums)
        nums.sort()
        res = []
        i = 0
        while i < N - 3:
            j = i + 1
            while j < N - 2:
                k = j + 1
                l = N - 1
                remain = target - nums[i] - nums[j]
                while k < l:
                    if nums[k] + nums[l] > remain:
                        l -= 1
                    elif nums[k] + nums[l] < remain:
                        k += 1
                    else:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        while k < l and nums[k] == nums[k + 1]:
                            k += 1
                        while k < l and nums[l] == nums[l - 1]:
                            l -= 1
                        k += 1
                        l -= 1

                while j < N - 2 and nums[j] == nums[j + 1]:
                    j += 1
                j += 1  # 重要
            while i < N - 3 and nums[i] == nums[i + 1]:
                i += 1
            i += 1  # 重要
        return res


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        O(n^3)
        """
        num = sorted(nums)
        n = len(nums)
        m = collections.defaultdict(list)
        res = set()

        for i in xrange(n-1):
            for j in xrange(i+1,n):
                m[num[i]+num[j]].append((i,j))

        for i in xrange(n-1):
            for j in xrange(i+1,n):
                rest = target-num[i]-num[j]
                for pair in m[rest]:
                    if i>pair[1]:
                        res.add((num[pair[0]], num[pair[1]], num[i], num[j]))

        return list(res)
