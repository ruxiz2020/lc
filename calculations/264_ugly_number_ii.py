def nthUglyNumber(self, n):
    dp = [1] * (n + 1)
    index2, index3, index5 = 1, 1, 1
    for i in range(2, n + 1):
        dp[i] = min(2 * dp[index2], 3 * dp[index3], 5 * dp[index5])
        if dp[i] == 2 * dp[index2]:
            index2 += 1
        if dp[i] == 3 * dp[index3]:
            index3 += 1
        if dp[i] == 5 * dp[index5]:
            index5 += 1
    return dp[-1]


import heapq
class Solution:
    def nthUglyNumber(self, n):
        s = {1, }
        q = []
        num = []
        heapq.heappush(q, 1)
        for i in range(n):
            cur = heapq.heappop(q)
            num.append(cur)
            for j in [2, 3, 5]:
                tmp = cur * j
                if tmp not in s:
                    s.add(tmp)
                    heapq.heappush(q, tmp)
        return num[n - 1]
