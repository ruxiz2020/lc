class Solution(object):
    ''' Once the current number is prime then all of it’s product is
    prime and the product must be smaller or equal than n.
    We marked such product in list as False.'''
    def countPrimes(self, n):
        if n < 2:
            return 0
        prime = [True] * n
        prime[0] = prime[1] = False
        for i in range(2, n):
            if prime[i]:
                for j in range(i + i, n, i):
                    prime[j] = False

        return prime.count(True)

n = 10
print("input: n = 10")

ss = Solution()
res = ss.countPrimes(n)
print("res:" + str(res))
