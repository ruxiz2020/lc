
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []



class Solution:
    '''O(n)'''
    def cloneGraph(self, node: Node) -> Node:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None


# Test Graph:
# 1 -- 2
# |    |
# 4 -- 3

def create_graph():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    return node1

# Test the Solution
original_graph = create_graph()
solution = Solution()
cloned_graph = solution.cloneGraph(original_graph)

# Function to print the graph for testing
def print_graph(node):
    visited = set()
    def dfs(n):
        if n in visited:
            return
        visited.add(n)
        print(f"Node {n.val} neighbors:", [nei.val for nei in n.neighbors])
        for nei in n.neighbors:
            dfs(nei)
    dfs(node)

print("Original graph:")
print_graph(original_graph)

print("\nCloned graph:")
print_graph(cloned_graph)
