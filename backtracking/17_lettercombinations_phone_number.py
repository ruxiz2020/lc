class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        O(4 ^N⋅N), O(N)
        """
        kvmaps = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        if digits:
            self.dfs(digits, 0, res, '', kvmaps)
        return res

    def dfs(self, input_string, index, res, path, kvmaps):
        if index == len(input_string):
            if path != '':
                res.append(path)
            return
        for j in kvmaps[input_string[index]]:
            self.dfs(input_string, index + 1, res, path + j, kvmaps)
