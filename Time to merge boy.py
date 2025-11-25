import random,time
start = time.time()
y=10
items = [random.randint(0,10000) for x in range(y)]
def merge_sort(arr):
    # Base case: a list of 0 or 1 elements is already sorted
    if len(arr) <= 1:
        return arr

    # Find the midpoint and split the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the two sorted halves together
    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []
    i = j = 0

    # Compare both lists and take the smallest item each time
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any remaining items (one of these will be empty)
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Example use:

sorted_numbers = merge_sort(items)
print("Sorted:", sorted_numbers)
end=time.time()
speed= round(end-start,5)
print(f'Time taken: {speed}')
