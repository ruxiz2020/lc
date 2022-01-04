class Solution(object):
    def findCircleNum(self, M):
        visited = set()
        count = 0

        def dfs(student, visited):
            for class_mate, is_friend in enumerate(M[student]):
                if class_mate not in visited and is_friend:
                    visited.add(class_mate)
                    dfs(class_mate, visited)

        for student in range(len(M)):
            if student not in visited:
                visited.add(student)
                count += 1
                dfs(student, visited)

        print(student)
        return count


if __name__ == '__main__':

    isConnected = [[1,0,0],[0,1,0],[0,0,1]]

    ss = Solution()
    res = ss.findCircleNum(isConnected)

    print(res)
