import heapq


def merge_sorted_arrays(arr1, arr2, arr3):
    # O(nlogk)
    # Combine all three arrays into a min-heap
    merged_array = []
    heap = []

    # Push the first element of each array into the heap along with its index and array id
    if arr1: heapq.heappush(heap, (arr1[0], 0, arr1))
    if arr2: heapq.heappush(heap, (arr2[0], 0, arr2))
    if arr3: heapq.heappush(heap, (arr3[0], 0, arr3))

    # Extract elements from the heap and push the next element from the same array
    while heap:
        val, idx, arr = heapq.heappop(heap)
        merged_array.append(val)
        if idx + 1 < len(arr):  # If there are more elements in the array
            heapq.heappush(heap, (arr[idx + 1], idx + 1, arr))

    return merged_array




def merge_two_sorted_arrays(a, b):
    """
    Merge two sorted arrays using a two-pointer approach.
    Returns a single sorted array containing all elements of a and b.
    O(n1 + n2 + n3)
    """
    merged = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    # Append any remaining elements
    while i < len(a):
        merged.append(a[i])
        i += 1
    while j < len(b):
        merged.append(b[j])
        j += 1

    return merged

def merge_sorted_arrays(arr1, arr2, arr3):
    """
    Merge three sorted arrays by first merging arr1 and arr2,
    then merging the result with arr3.
    """
    merged12 = merge_two_sorted_arrays(arr1, arr2)
    merged123 = merge_two_sorted_arrays(merged12, arr3)
    return merged123



# Example usage
arr1 = [1, 4, 7]
arr2 = [2, 5, 8]
arr3 = [3, 6, 9, 10]

merged_array = merge_sorted_arrays(arr1, arr2, arr3)
print(merged_array)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
