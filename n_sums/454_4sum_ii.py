from collections import defaultdict

class Solution:
    def fourSumCount(self, A, B, C, D):
        ct = defaultdict(int)
        for a in A:
            for b in B:
                ct[a + b] += 1
        res = 0
        for c in C:
            for d in D:
                if -(c + d) in ct:
                    res += ct[-(c + d)]
        print(ct)
        return res

if __name__ == '__main__':

    nums1 = [1,2]; nums2 = [-2,-1]; nums3 = [-1,2]; nums4 = [0,2]
    ss = Solution()
    res = ss.fourSumCount(nums1, nums2, nums3, nums4)

    print(res)
