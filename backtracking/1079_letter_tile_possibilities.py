from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # Helper function to perform depth-first search on tile counts.
        def dfs(tile_counter: Counter) -> int:
            combinations_count = 0  # Initialize the count of combinations.

            # Iterate through each tile in the counter.
            for tile, count in tile_counter.items():
                # If there is at least one tile available, use one to form a new sequence.
                if count > 0:
                    combinations_count += 1  # Include this tile as a new possibility.
                    tile_counter[tile] -= 1  # Use one tile.

                    # Recursively count further possibilities by using the recently used tile.
                    combinations_count += dfs(tile_counter)

                    # Undo the choice to backtrack and allow for different combinations.
                    tile_counter[tile] += 1

            # Return the total number of combinations.
            return combinations_count

        # Count the occurrences of each tile.
        tile_counter = Counter(tiles)

        # Start DFS with the count of available tiles to find all possible combinations.
        return dfs(tile_counter)
