import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        m * nlogn
        """
        res = collections.defaultdict(list)
        for string in strs:
            sorted_str = ''.join(sorted(string))
            res[sorted_str].append(string)
        return res.values()

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        hashmap
        O( m * n * 26 )
        """
        '''mapping charCount tp list of Anagram'''
        res = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)

        return res.values()
