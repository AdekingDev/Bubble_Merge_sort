import random

def bubble_sort(arr):
    n = len(arr)
    operations = 0
    total_expected_operations = n * (n - 1) // 2  
    print_interval = total_expected_operations // 5 

    for i in range(n):
        for j in range(0, n-i-1):
            operations += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            
            if operations % print_interval == 0 or operations == total_expected_operations:
                print(f"Bubble Sort Step {operations}: {arr}")

    return arr, operations

def merge_sort(arr, l, r, operations=0):
    print_interval = 20 

    if l < r:
        m = l + (r - l) // 2

        # Sort first and second halves
        operations = merge_sort(arr, l, m, operations)
        operations = merge_sort(arr, m + 1, r, operations)

        # Merge the sorted halves
        operations, _ = merge(arr, l, m, r, operations, print_interval)

    return operations

def merge(arr, l, m, r, operations, print_interval):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
        operations += 1

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
        operations += 1

    # Merge the temp arrays back into arr[l..r]
    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
        operations += 1

        if operations % print_interval == 0:
            print(f"Merge Sort Step {operations}: {arr}")

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        operations += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
        operations += 1

    return operations, arr

# Create an array of 100 integers
array = [random.randint(1, 100) for _ in range(100)]

# Bubble sort
print("Starting Bubble Sort:")
sorted_array_bubble, operations_bubble = bubble_sort(array.copy())

# Merge sort
print("\nStarting Merge Sort:")
operations_merge = merge_sort(array.copy(), 0, len(array) - 1)

print("\nBubble Sort Operations:", operations_bubble)
print("Merge Sort Operations:", operations_merge)
