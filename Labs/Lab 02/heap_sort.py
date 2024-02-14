# Q- 1. (2.5 pts)

# The objective of this task is to implement the Heap Sort algorithm, understand its properties,
# and analyze its time complexity.
# 1. Heap Sort Implementation:
# • heapify: Implement a method to heapify a subtree rooted at a given index in the array representation of the heap.
# • build heap: Implement a method to build a Max Heap from an array of elements.
# • heap sort: Implement the Heap Sort algorithm using the Max Heap data structure.

# 2. Testing:
# Test your implementation with different input scenarios, including:
# • Random arrays of varying sizes.
# • Arrays with duplicate elements.
# • Sorted arrays (ascending and descending).
# • Arrays with negative numbers.
# • Verify that Heap Sort produces correct output for each input scenario.

# Analyze the time complexity of Heap Sort, explain in details.
import numpy as np


def max_heapify(arr, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)


def build_heap(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)


def heap_sort(arr):
    n = len(arr)

    build_heap(arr)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)


# Testing the implementation
# Random array
arr1 = np.random.randint(100, size=10)
heap_sort(arr1)
print("Random array:", arr1)

# Duplicate elements
arr2 = np.random.randint(100, size=10)
heap_sort(arr2)
print("Duplicate elements:", arr2)

# Sorted arrays (ascending and descending)
arr3 = np.random.randint(100, size=10)
heap_sort(arr3)
print("Sorted arrays:", arr3)

# Negative numbers
arr4 = np.random.randint(-100, 100, size=10)
heap_sort(arr4)
print("Negative numbers:", arr4)



