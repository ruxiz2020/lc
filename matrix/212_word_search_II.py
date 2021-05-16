class Solution:
    def findWords(self, board, words):
        def dfs(x, y, root):
            letter = board[x][y]
            cur = root[letter]
            word = cur.pop('#', False)
            if word:
                res.append(word)
            board[x][y] = '*'
            for dirx, diry in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                curx, cury = x + dirx, y + diry
                if 0 <= curx < m and 0 <= cury < n and board[curx][cury] in cur:
                    dfs(curx, cury, cur)
            board[x][y] = letter
            if not cur:
                root.pop(letter)

        trie = {}
        for word in words:
            cur = trie
            for letter in word:
                cur = cur.setdefault(letter, {})
            cur['#'] = word
        print(trie)
        m, n = len(board), len(board[0])
        res = []
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(i, j, trie)
        return res


board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]

# trie:
# {'o': {'a': {'t': {'h': {'#': 'oath'}}}}, 'p': {'e': {'a': {'#': 'pea'}}},
# 'e': {'a': {'t': {'#': 'eat'}}}, 'r': {'a': {'i': {'n': {'#': 'rain'}}}}}

print("board:")
print(board)

print("words:")
print(words)

ss = Solution()
res = ss.findWords(board, words)

print(res)
