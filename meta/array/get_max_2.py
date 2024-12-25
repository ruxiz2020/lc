
def get_max_two(l):
    """
    This function iterates through the list 'l' and keeps track of:
    - cur_max: The maximum element seen so far (while traversing).
    - cur_max_sum: The maximum sum found so far using 'cur_max' and a future element.

    The loop checks possible sums of pairs where the second element of
    the pair is one step ahead in the list (i+1), thus skipping the direct adjacency.

    :param l: A list of integers
    :return: An integer representing the maximum sum of two elements
             under the given constraints.
    """

    # Initialize cur_max with the first element.
    cur_max = l[0]

    # Initialize cur_max_sum to 0 (the maximum sum so far).
    cur_max_sum = 0

    # Iterate from index 1 to second last index (since we'll use i+1).
    for i in range(1, len(l) - 1):
        # Update cur_max_sum by comparing its current value
        # with the sum of cur_max and the element at l[i + 1].
        # Essentially, this tries pairing the current maximum element
        # we have seen so far with the next element in the list (i+1).
        cur_max_sum = max(cur_max_sum, cur_max + l[i + 1])

        # Update cur_max to be the maximum of the current cur_max
        # and the element at l[i]. In other words,
        # we move forward and see if l[i] is a new maximum.
        cur_max = max(cur_max, l[i])

        # Debug print to see intermediate states of cur_max_sum and cur_max.
        print(cur_max_sum, cur_max)

    # Return the maximum sum found.
    return cur_max_sum



l = [200, 300, 105, 10, 6]

res = get_max_two(l)
print(res) # 310
