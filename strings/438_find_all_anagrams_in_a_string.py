from collections import Counter


class Solution:
    def findAnagrams(self, s, p):
        answer = []
        m, n = len(s), len(p)
        if m < n:
            return answer
        pCounter = Counter(p)
        sCounter = Counter(s[:n - 1])
        index = 0
        for index in range(n - 1, m):
            sCounter[s[index]] += 1
            if sCounter == pCounter:
                answer.append(index - n + 1)
            sCounter[s[index - n + 1]] -= 1
            if sCounter[s[index - n + 1]] == 0:
                del sCounter[s[index - n + 1]]
        return answer


if __name__ == '__main__':

    s = "cbaebabacd"
    p = "abc"

    ss = Solution()
    res = ss.findAnagrams(s, p)
    print(res)
