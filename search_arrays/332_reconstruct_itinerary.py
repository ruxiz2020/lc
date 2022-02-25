from collections import defaultdict

class Solution:
    def findItinerary(self, tickets):
        def dfs(dep):
            arr = paths[dep]
            while arr:
                dfs(arr.pop())
            res.append(dep)

        res = []
        paths = defaultdict(list)
        tickets.sort(key=lambda x: x[1], reverse=True)
        for s, t in tickets:
            paths[s].append(t)
        print(paths)
        dfs('JFK')
        print(res)
        return res[::-1]


if __name__ == '__main__':

    tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

    ss = Solution()
    res = ss.findItinerary(tickets)

    print(res)
