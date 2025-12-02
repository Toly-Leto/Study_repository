from random import randint
from time import time
M = 12            # максимальная мощность одного множества
N = 3            # число множеств
min_num = 0
max_num = 15     # верхняя граница для значений (включительно)


def make_set(max_size):
    size = randint(1, max_size)
    new_set = set()
    while len(new_set) < size:
        new_set.add(randint(min_num, max_num))
    return new_set


def generate_sets(max_size, count):
    return [make_set(max_size) for _ in range(count)]


def get_max_intersection_for_set(all_sets, a_set):
    best = set()
    for s in all_sets:
        if s is a_set:
            continue
        inter = s & a_set
        if len(inter) > len(best):
            best = inter
    return best


def main_intersection(all_sets):
    best_overall = set()
    n = len(all_sets)
    for i in range(n):
        for j in range(i+1, n):
            inter = all_sets[i] & all_sets[j]
            if len(inter) > len(best_overall):
                best_overall = inter

    return best_overall


lst = generate_sets(M, N)
start = time()
res_1 = main_intersection(lst)
end = time()
elapsed = end - start


print(lst)
print(f"{'Число множеств:':.<60}{N}")
print(f"{'Максимальное число элементов множества:':.<60}{M}")
print(f"{'Максимальная мощность пересечения множеств:':.<60}{len(res_1)}")
print(f"{'Искомое множество:':.<60}{res_1}")
print(f"{'Время поиска максимальной мощности пересечения множеств:':.<60}{elapsed:.9f}")


