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

# Example usage
arr1 = [1, 4, 7]
arr2 = [2, 5, 8]
arr3 = [3, 6, 9, 10]

merged_array = merge_sorted_arrays(arr1, arr2, arr3)
print(merged_array) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
