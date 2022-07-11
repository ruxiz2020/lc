import heapq
import collections


class Solution:
    '''Dijkstra's (BFS with min heap) - shortest path graph algo
    O(E * log(V ^ 2))'''
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            if u == v:
                return -1
            graph[u].append((v, w))
        if K not in graph:
            return -1

        pq = [(0, K)] # min heap
        visit = {}
        while pq:
            step, source = heapq.heappop(pq)
            if source in visit:
                continue
            visit[source] = step
            for target, distance in graph[source]:
                if target not in visit:
                    heapq.heappush(pq, (step + distance, target))
        return max(visit.values()) if len(visit) == N else -1
