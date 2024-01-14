class Solution:
    def numRollsToTarget(self, dice: int, sides: int, target: int) -> int:
        # Initialize the array of ways to achieve each sum, with 1 way to achieve a sum of 0
        ways_to_achieve_sum = [1] + [0] * target
        # Define the modulo according to the problem statement to avoid large numbers
        modulo = 10**9 + 7

        # Iterate through each dice
        for i in range(1, dice + 1):
            # Initialize the temporary array for the current dice's sum calculations
            current_ways = [0] * (target + 1)
            # Calculate the number of ways to achieve each sum with the current number of dice
            for sum_value in range(1, min(i * sides, target) + 1):
                # Calculate the ways to get to this sum_value using the previous number of dice
                for face_value in range(1, min(sum_value, sides) + 1):
                    current_ways[sum_value] = (current_ways[sum_value] + ways_to_achieve_sum[sum_value - face_value]) % modulo
            # Update the array of ways with the current dice's calculation
            ways_to_achieve_sum = current_ways

        # Return the total number of ways to achieve the target sum with all dice
        return ways_to_achieve_sum[target]
