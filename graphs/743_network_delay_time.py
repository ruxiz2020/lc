import connectionsm heapq

class Solution:
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            if u == v:
                return -1
            graph[u].append((v, w))
        if K not in graph:
            return -1

        pq = [(0, K)]
        dict = {}
        while pq:
            step, source = heapq.heappop(pq)
            if source in dict:
                continue
            dict[source] = step
            for target, distance in graph[source]:
                if target not in dict:
                    heapq.heappush(pq, (step + distance, target))
        return max(dict.values()) if len(dict) == N else -1
