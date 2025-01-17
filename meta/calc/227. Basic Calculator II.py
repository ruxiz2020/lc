# Author: Huahua
class Solution:
    """
    O(n)
    O(n)
    """
    def calculate(self, s: str) -> int:
        nums = []
        op = '+'
        cur = 0
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            while i < len(s) and s[i].isdigit():
                cur = cur * 10 + ord(s[i]) - ord('0')
                i += 1
            if op in '+-':
                nums.append(cur * (1 if op == '+' else -1))
            elif op == '*':
                nums[-1] *= cur
            elif op == '/':
                # sign = -1 if nums[-1] < 0 or cur < 0 else 1
                sign = -1 if (nums[-1] < 0) != (cur < 0) else 1
                print(abs(cur), sign)
                nums[-1] = abs(nums[-1]) // abs(cur) * sign
            cur = 0
            if (i < len(s)): op = s[i]
            i += 1
        print(nums)
        return sum(nums)


ss = Solution()
s = "3-2*2"
s = "5-3/2"
res = ss.calculate(s)
print(res)  # 4
