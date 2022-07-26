import collections

class Node(object):
    def __init__(self):
        self.children = {}
        self.isword = False

class Trie(object):

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current = self.root
        for w in word:
            if w not in current.children:
                current.children[w] = Node()
            current = current.children[w]
        current.isword = True

    def search(self, word):
        current = self.root
        for w in word:
            current = current.children.get(w)
            if current == None:
                return False
        return current.isword

    def startsWith(self, prefix):
        current = self.root
        for w in prefix:
            current = current.children.get(w)
            if current == None:
                return False
        return True


#act = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]

trie = Trie();
trie.insert("apple");
print(trie.root.children)
print(trie.search("apple"));   # return True
print(trie.search("app"));     # return False
print(trie.startsWith("app")); # return True
trie.insert("app");
print(trie.search("app"));     # return True
