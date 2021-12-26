import collections


class MagicDictionary(object):

    def _candidate(self, word):
        for i in range(len(word)):
            yield word[:i] + '*' + word[i + 1:]

    def buildDict(self, words):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        self.words = set(words)

        self.near = collections.Counter([word for word in words for word in self._candidate(word)])
        print(self.near)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        print(list(self._candidate(word)))
        return any(self.near[cand] > 1 or self.near[cand] == 1 and word not in self.words for cand in self._candidate(word))


# Your MagicDictionary object will be instantiated and called as such:
obj = MagicDictionary()

dict = ["hello", "leetcode"]
word = "hlllo"
obj.buildDict(dict)
param_2 = obj.search(word)

print(param_2)
