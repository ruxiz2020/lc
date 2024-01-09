from collections import defaultdict
from typing import List


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        # Build a graph where each node represents a garden and edges represent paths
        graph = defaultdict(list)
        for path in paths:
            # Decrementing by 1 to convert the 1-indexed gardens to 0-indexed for easier array manipulation
            a, b = path[0] - 1, path[1] - 1
            graph[a].append(b)
            graph[b].append(a)

        # Initialize the answer array where each garden's flower type will be stored
        garden_flower_types = [0] * n

        # Loop through each garden and choose a flower type
        for garden in range(n):
            # Build a set of used flower types for the current garden's adjacent gardens
            used_flower_types = {garden_flower_types[adj] for adj in graph[garden]}

            # Assign the lowest flower type (1-4) that is not used by adjacent gardens
            for flower_type in range(1, 5):
                if flower_type not in used_flower_types:
                    garden_flower_types[garden] = flower_type
                    break

        # Return the list of assigned flower types for each garden
        return garden_flower_types
