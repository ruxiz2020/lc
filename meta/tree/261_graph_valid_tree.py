class Solution:
    """
    This code checks whether a given undirected graph is a valid tree by 
    using Depth-First Search (DFS) to ensure the graph is connected 
    (all nodes are reachable from a starting node) and acyclic (no cycles exist).

    It first builds an adjacency list to represent the graph, 
    then recursively traverses the graph from node 0, 
    marking nodes as visited and checking for cycles by avoiding 
    revisiting already visited nodes, except the immediate parent.

    The algorithm returns True if the DFS visits all nodes 
    exactly once (ensuring connectivity) and finds no cycles; it runs in 
    O(N+E) time and uses 
    O(N) space for the adjacency list and visited set, where 
    N is the number of nodes and 
    E the number of edges.

    Time Complexity: O(N)
      - Building the adjacency list and traversing the graph is O(N + E) where E ~ N - 1 for a tree.
    Space Complexity: O(N)
      - We store the adjacency list and a 'visit' set of size up to N.
    """
    def validTree(self, n, edges):
        # Edge case: if n == 0, we consider it trivially true (or handle by definition).
        if not n:
            return True

        # 1. Build adjacency list for all nodes from 0..n-1
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        # Example: if edges = [[0,1],[0,2],[0,3],[1,4]],
        # adj might look like {0: [1, 2, 3], 1: [0, 4], 2: [0], 3: [0], 4: [1]}

        # A set to keep track of visited nodes in DFS
        visit = set()

        def dfs(node, prev):
            """
            DFS that returns False if a cycle is detected, otherwise True.
            'node' is the current node,
            'prev' is the node we came from to avoid backtracking being mistaken for a cycle.
            """
            # If node is already visited, we found a cycle
            if node in visit:
                return False

            # Mark current node as visited
            visit.add(node)

            # Explore all adjacent neighbors
            for neighbor in adj[node]:
                # Skip the edge to the parent node in DFS
                if neighbor == prev:
                    continue
                # If DFS on neighbor returns False, it means a cycle was found or error
                if not dfs(neighbor, node):
                    return False
            # If no cycle found in this path, return True
            return True

        # 2. Start DFS from node 0 (arbitrary choice since all nodes should be connected).
        # If DFS returns True (no cycle) AND we visited exactly n nodes,
        # then it's a valid tree (connected and acyclic).
        return dfs(0, -1) and len(visit) == n



if __name__ == '__main__':

    n = 5
    edges = [[0,1],[0,2],[0,3],[1,4]]

    ss = Solution()
    res = ss.validTree(n, edges)
    print(res)
