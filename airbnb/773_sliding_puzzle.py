class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        goal = "123450"
        start = ''
        for i in range(2):
            for j in range(3):
                start += str(board[i][j])
        q = collections.deque()
        q.append((start,0))
        visited = set()
        visited.add(start)

        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        while q:
            path,step = q.popleft()
            if path == goal:
                return step
            pos = path.index('0')
            i,j = pos//3,pos%3
            path = list(path)
            for d in dirs:
                x = i+d[0]
                y = j+d[1]
                if x<0 or x>=2 or y<0 or y>=3:
                    continue
                path[x*3+y],path[i*3+j] = path[i*3+j],path[x*3+y]
                pathstr = ''.join(path)
                if pathstr not in visited:
                    q.append((pathstr,step+1))
                    visited.add(pathstr)
                path[x*3+y],path[i*3+j] = path[i*3+j],path[x*3+y]
        return -1
