import random
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def randomized_quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

def deterministic_quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[len(arr) // 2]  
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

def measure_time(sort_function, arr, iterations=5):
    times = []
    for _ in range(iterations):
        arr_copy = arr.copy()
        start_time = time.perf_counter()
        sort_function(arr_copy)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return np.mean(times)

array_sizes = [10_000, 50_000, 100_000, 500_000]
results = []

for size in array_sizes:
    arr = [random.randint(0, 1_000_000) for _ in range(size)]
    randomized_time = measure_time(randomized_quick_sort, arr)
    deterministic_time = measure_time(deterministic_quick_sort, arr)
    print(f"\nРозмір масиву: {size}")
    print(f"   Рандомізований QuickSort: {randomized_time:.4f} секунд")
    print(f"   Детермінований QuickSort: {deterministic_time:.4f} секунд")
    results.append((size, randomized_time, deterministic_time))

df = pd.DataFrame(results, columns=["Розмір масиву", "Час (рандомізований)", "Час (детермінований)"])

df.to_csv("quicksort_results.csv", index=False)

plt.figure(figsize=(10, 6))
plt.plot(df["Розмір масиву"], df["Час (рандомізований)"], marker='o', label="Рандомізований QuickSort")
plt.plot(df["Розмір масиву"], df["Час (детермінований)"], marker='s', label="Детермінований QuickSort")
plt.xlabel("Розмір масиву")
plt.ylabel("Середній час виконання (секунди)")
plt.title("Порівняння продуктивності QuickSort")
plt.legend()
plt.grid(True)
plt.show()
