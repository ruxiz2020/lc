class Solution:
    def findLongestWord(self, s, d):
        def helper(s, target):
            i = 0
            j = 0
            while i < len(s) and j < len(target):
                if s[i] == target[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            return j == len(target)
            d.sort(key=lambda x: [-len(x), x])
        for dict_ in d:
            if helper(s, dict_):
                return dict_
        return ''
