class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        target = [0] * 128
        for c in t: target[ord(c)] += 1

        cnt, start = len(t), 0
        ans_s, ans_e = 0, len(s) + 1

        for i in range(len(s)):
            if target[ord(s[i])] > 0:
                cnt -= 1
            target[ord(s[i])] -= 1

            while cnt == 0:
                if i - start < ans_e - ans_s:
                    ans_s, ans_e = start, i

                if target[ord(s[start])] == 0:
                    cnt += 1
                target[ord(s[start])] += 1
                start += 1
        return "" if ans_e - ans_s + 1 > len(s) else s[ans_s: ans_e + 1]
