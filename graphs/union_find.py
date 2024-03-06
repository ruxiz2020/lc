class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]  # Initialize each element as its own parent
        self.rank = [0] * n  # Initialize rank of each element as 0

    def find(self, x):
        if self.parent[x] != x:
            # Path compression: Set the parent of x to its root parent
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        # Union by rank: Attach smaller rank tree under root of higher rank tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

# Example usage:
n = 6
uf = UnionFind(n)

uf.union(0, 1)
uf.union(1, 2)
uf.union(3, 4)
uf.union(4, 5)

print("Parent array:", uf.parent)
# Output: [0, 0, 0, 3, 3, 3]
