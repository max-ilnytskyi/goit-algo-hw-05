def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            return (iterations, arr[mid])
        elif arr[mid] < target:
            low = mid + 1
        else:
            upper_bound = arr[mid]
            high = mid - 1

    return (iterations, upper_bound)


sorted_arr = [1.2, 2.4, 3.5, 4.8, 6.0, 7.3, 8.9]
target = 1.5
result = binary_search(sorted_arr, target)
print(result)
