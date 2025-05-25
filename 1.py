import random
import time
import matplotlib.pyplot as plt
import numpy as np

# Рандомізований QuickSort
def randomized_quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

# Детермінований QuickSort (перший елемент як pivot)
def deterministic_quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

# Функція для вимірювання середнього часу виконання
def measure_time(sort_func, arr, repeats=5):
    times = []
    for _ in range(repeats):
        copy_arr = arr[:]
        start = time.perf_counter()
        sort_func(copy_arr)
        end = time.perf_counter()
        times.append(end - start)
    return sum(times) / repeats

# Основні параметри
sizes = [10000, 50000, 100000, 500000]
randomized_times = []
deterministic_times = []

# Вимірювання часу виконання для кожного розміру
for size in sizes:
    arr = [random.randint(0, 1000000) for _ in range(size)]
    print(f"Розмір масиву: {size}")
    avg_r = measure_time(randomized_quick_sort, arr)
    print(f"   Рандомізований QuickSort: {avg_r:.4f} секунд")
    randomized_times.append(avg_r)

    avg_d = measure_time(deterministic_quick_sort, arr)
    print(f"   Детермінований QuickSort: {avg_d:.4f} секунд\n")
    deterministic_times.append(avg_d)

# Побудова графіку
plt.figure(figsize=(10, 6))
plt.plot(sizes, randomized_times, label="Randomized QuickSort", marker='o')
plt.plot(sizes, deterministic_times, label="Deterministic QuickSort", marker='s')
plt.xlabel("Розмір масиву")
plt.ylabel("Середній час виконання (секунди)")
plt.title("Порівняння Randomized vs Deterministic QuickSort")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Повертаємо результати у вигляді таблиці
list(zip(sizes, randomized_times, deterministic_times))