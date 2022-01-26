import heapq
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ans = [1] * n
        q = [[prime, 0, prime] for prime in primes]
        heapq.heapify(q)

        for i in range(1, n):
            print(q)
            cur = heapq.heappop(q)
            ans[i] = cur[0]
            while q and q[0][0] == ans[i]:
                t = heapq.heappop(q)
                t[1] += 1
                t[0] = ans[t[1]] * t[2]
                heapq.heappush(q, t)
            cur[1] += 1
            #print(cur, ans)
            cur[0] = ans[cur[1]] * cur[2]
            heapq.heappush(q, cur)
        return ans[n - 1]


if __name__ == '__main__':

    n = 5; primes = [2,3,5]

    ss = Solution()
    res = ss.nthSuperUglyNumber(n, primes)

    print(res)
