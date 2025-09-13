# ===============================================
# ALGORITHMIC COMPLEXITY EXAMPLES IN PYTHON
# ===============================================

# O(1) – Constant time
# Accessing the first element of a list is a constant-time operation.
def get_first_element(lst):
    # Always takes the same time, regardless of list size
    return lst[0]

# O(log n) – Logarithmic time
# Binary search divides the search space by 2 each time (must be sorted).
def binary_search(lst, target):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# O(n) – Linear time
# Looping through a list once is linear time.
def find_max(lst):
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

# O(n log n) – Linearithmic time
# Merge sort uses divide-and-conquer to sort efficiently.
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left or right)
    return result

# O(n²) – Quadratic time
# Bubble sort compares every element with every other: two nested loops.
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

# O(2ⁿ) – Exponential time
# Recursive Fibonacci grows rapidly in function calls.
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# O(n!) – Factorial time
# Generating all permutations of n elements.
from itertools import permutations

def all_permutations(lst):
    return list(permutations(lst))

# =======================
# DEMO AND PRINT RESULTS
# =======================

if __name__ == "__main__":
    sample_list = [3, 1, 4, 1, 5, 9]
    sorted_list = sorted(sample_list)

    print("O(1) – First element:", get_first_element(sample_list))
    print("O(log n) – Binary search (5):", binary_search(sorted_list, 5))
    print("O(n) – Max element:", find_max(sample_list))
    print("O(n log n) – Merge sort:", merge_sort(sample_list[:]))
    print("O(n²) – Bubble sort:", bubble_sort(sample_list[:]))
    print("O(2ⁿ) – Fibonacci(10):", fibonacci(10))  # Be careful with large n
    print("O(n!) – Permutations of [1, 2, 3]:", all_permutations([1, 2, 3]))

