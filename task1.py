import random
import timeit

def insertion_sort(arr):
    """Сортування масиву методом вставки."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    """Сортування масиву методом злиття."""
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Тестування алгоритмів сортування та вимірювання часу виконання
sizes = [100, 1000, 5000, 10000]
results = {"Insertion Sort": [], "Merge Sort": [], "Timsort": []}

for size in sizes:
    setup_code = f"""
from __main__ import insertion_sort, merge_sort
import random
arr = [random.randint(0, {size}) for _ in range({size})]
"""

    # Вимірювання часу для сортування вставками
    t_insertion = timeit.timeit('insertion_sort(arr.copy())', setup=setup_code, number=1, globals=globals())
    results["Insertion Sort"].append(t_insertion)

    # Вимірювання часу для сортування злиттям
    t_merge = timeit.timeit('merge_sort(arr.copy())', setup=setup_code, number=1, globals=globals())
    results["Merge Sort"].append(t_merge)

    # Вимірювання часу для Timsort
    t_timsort = timeit.timeit('sorted(arr.copy())', setup=setup_code, number=1, globals=globals())
    results["Timsort"].append(t_timsort)

print(results)
