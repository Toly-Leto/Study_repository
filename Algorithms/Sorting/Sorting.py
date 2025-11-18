from random import *
from time import *
N = [randint(1, 1000) + randint(1, 1000) for _ in range(4000)]
res = sorted(N)


def show_time(func):
    def wrapper(lst):
        start = time()
        result = func(lst)
        end = time()
        timer = end - start
        return func.__name__, timer, result
    return wrapper


@show_time
def Py_sort(lst):
    return sorted(lst), 1, 1

@show_time
def Boble_sort(lst):
    C = 0
    M = 0
    l = len(lst)
    for i in range(l):
        for j in range(l - i - 1):
            C += 1
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                M += 1
    return lst, C, M

@show_time
def selection_sort(arr):
    C = 0
    M = 0
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            C += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        M += 1
    return arr, C, M


@show_time
def Merge_sort(lst):
    return merge_sort(lst), 1, 1

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)

def _merge(left, right):
    i = j = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    if i < len(left):
        merged.extend(left[i:])
    if j < len(right):
        merged.extend(right[j:])
    return merged


@show_time
def Quick_sort(arr):
    return quicksort(arr), 1, 1

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


def table():
    lst = [Boble_sort(list(N)), Merge_sort(list(N)), selection_sort(list(N)), Quick_sort(list(N)), Py_sort(list(N))]

    print(f' {"_" * 25:25} {"_" * 25:25} {"_" * 25:25} {"_" * 25:25} {"_" * 25:25} {"_" * 25:25} {"_" * 25:25} ')
    print(f'|{"Название алгоритма":25}|{"Время выполнения (сек)":25}|{"Относительная скорость":25}|{"Корректность":25}|'
          f'{"Количество операций ":25} {"Количество перестановок":25} {"С/M":25}| ')
    print(f'|{"-"*25:25}|{"-"*25:25}|{"-"*25:25}|{"-"*25:25}|{"-"*25:25}|{"-"*25:25}|{"-"*25:25}|')

    times = [lst[0][1], lst[1][1], lst[2][1], lst[3][1], lst[4][1]]
    min_time = min(times)
    for line in lst:
        name, timer, lst_ = line
        print(f'|{name:<25}|{timer:<25.6f}|{timer/min_time:<25.6f}|{lst_[0] == res:<25}|'
              f'{lst_[1]:25}|{lst_[2]:25}|{lst_[1]/lst_[2]:25}|')

        print(f'|{"-" * 25:25}|{"-" * 25:25}|{"-" * 25:25}|{"-" * 25:25}|'
              f'{"-" * 25:25}|{"-" * 25:25}|{"-" * 25:25}|')


table()