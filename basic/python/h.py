def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[pi] is now at right place
        pi = partition(arr, low, high)
        
        # Recursively sort elements before and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def partition(arr, low, high):
    # Choose the rightmost element as pivot
    pivot = arr[high]
    
    # Index of smaller element
    i = low - 1
    
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            # Increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Swap the pivot element with the element at i + 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array:", arr)
