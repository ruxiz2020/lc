def missingElement(nums, k):
    missing_count = 0
    i = 1

    while i < len(nums):
        expected = nums[i - 1] + 1
        while expected < nums[i]:
            missing_count += 1
            if missing_count == k:
                return expected
            expected += 1
        i += 1

    # If kth missing number is not within the array, extrapolate
    return nums[-1] + (k - missing_count)
