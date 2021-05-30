class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        字典树，在查找的时候，使用dfs，如果遇到点，要遍历所有子树
        """

        self.trie = {}

    def addWord(self, word):
        """ Adds a word into the data structure. """
        cur = self.trie
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = True

    def search(self, word) :
        """ Returns if the word is in the data structure.
        A word could contain the dot character '.' to represent any one letter. """
        return self.dfs(self.trie, word, 0)

    def dfs(self, node, word, i):
        if i == len(word):
            return '#' in node
        if word[i] == '.':
            for child in node:
                if child != '#' and self.dfs(node[child], word, i + 1):
                    return True
            return False

        if word[i] not in node:
            return False
        return self.dfs(node[word[i]], word, i + 1)
