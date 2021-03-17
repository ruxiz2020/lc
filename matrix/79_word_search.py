class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        O(N 3^L)
        """
        def dfs(x, y, p):
            if p == l:
                return True
            for dirx, diry in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                curx, cury = x + dirx, y + diry
                if 0 <= curx < m and 0 <= cury < n and flag[curx][cury] and board[curx][cury] == word[p]:
                    flag[curx][cury] = False
                    if dfs(curx, cury, p + 1):
                        flag[curx][cury] = True
                        return True
                    flag[curx][cury] = True
            return False

        m, n = len(board), len(board[0])
        l = len(word)
        flag = [[True] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    flag[i][j] = False
                    if dfs(i, j, 1):
                        return True
                    flag[i][j] = True
        return False
