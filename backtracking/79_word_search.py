class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        O(m * n * dfs(4 ^ len(word)))
        """
        m, n = len(board), len(board[0])
        paths = set()
        def dfs(x, y, p):
            if p == len(word):
                return True
            if (x < 0 or y < 0 or x >= m or y >= n or \
                word[p] != board[x][y] or (x, y) in paths):
                return False
            paths.add((x, y))
            res = (dfs(x + 1, y, p + 1) or \
                   dfs(x - 1, y, p + 1) or \
                   dfs(x, y + 1, p + 1) or \
                   dfs(x, y - 1, p + 1))
            paths.remove((x, y))
            return res

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False

if __name__ == '__main__':

    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"

    ss = Solution()
    res = ss.exist(board, word)

    print(res)
