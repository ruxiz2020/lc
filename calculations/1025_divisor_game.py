class Solution(object):
    def divisorGame(self, N):
        dp = [False for i in range(N+1)]
        dp[1] = False
        dp[0] = True
        for i in range(2, N + 1):
            for j in range(1, N // 2 + 1):
                if i % j == 0 and (not dp[i - j]):
                    dp[i] = True
                    break
        return dp[-1]

class Solution(object):
    def divisorGame(self, n):
        # 1: False
        # 2: True
        # 3: False
        # 4: choose from (1,2) -- 4-3 = 1, False so Alice is True; 4-2 = 2, True so Alice is False -- True
        # 5: choose from (1) -- 5-1 = 4, True so Alice is False -- False
        # Induction:
        # For any even number, can choose 1 so that Bob is left with an odd (False), so Alice can win
        # For any odd number, can only choose odd divisors to substract, resulting in Bob getting an even, so Bob can win, and Alice loses
        return n % 2 == 0
