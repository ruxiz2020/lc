class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
    def isOk(self,row, col):
        for i in range(0, row):
            if(col == self.column[i] or abs(row - i) == abs(col - self.column[i])):
                return False
        return True

    def queue(self, row):
        if(row == self.n):
            self.total += 1
        else:
            for col in range(0, self.n):
                self.column[row] = col
                if(self.isOk(row, col)):
                    self.queue(row + 1)

    def totalNQueens(self, n):
        self.total = 0
        self.n = n
        self.column = [0] * self.n
        self.queue(0)
        return self.total
