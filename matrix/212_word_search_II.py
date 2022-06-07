class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board, words):
        root = TrieNode()
        for w in words:
            root.addWord(w)


        m, n = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(x, y, node, word):

            if (x < 0 or y < 0 or x == m or y == n or \
                (x, y) in visit or board[x][y] not in node.children):
                return

            visit.add((x, y))
            node = node.children[board[x][y]]
            word += board[x][y]

            if node.isWord:
                res.add(word)

            dfs(x + 1, y, node, word)
            dfs(x - 1, y, node, word)
            dfs(x, y + 1, node, word)
            dfs(x, y - 1, node, word)
            visit.remove((x, y))


        for i in range(m):
            for j in range(n):
                dfs(i, j, root, "")

        return list(res)



if __name__ == '__main__':
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]

    ss = Solution()
    res = ss.findWords(board, words)

    print(res)
