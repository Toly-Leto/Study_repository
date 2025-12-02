from random import *
from time import  time


M = 500
N = 100
min_num = 0
max_mun = 10000

def make_set(M):
    m = randint(1, M)
    new_set = set()
    while len(new_set) < m:
        new_num = randint(min_num, max_mun)
        new_set.add(new_num)
    return new_set


def ganerat_sets(M, N):
    res = [make_set(M) for j in range(N)]
    return res

def get_max_intersectino(lst_of_sets:list, a_set):
    lst_of_int_set = []
    lst_of_sets.remove(a_set)
    for new_set in lst_of_sets:
        lst_of_int_set += [new_set & a_set]
    return max(lst_of_int_set, key=len)

def main_intersection(lst_of_sets):
    res_list = []
    for i_set in lst_of_sets:
        max_for_i = get_max_intersectino(lst_of_sets, i_set)
        res_list += [max_for_i]
    return max(res_list, key=len)



lst = ganerat_sets(M, N)


start = time()
res_1 = main_intersection(lst)
end = time()
res_2 = end - start
print()
print(f"{'Число множеств:':.<60}{N}")
print(f"{'Максимальное число элементов множества:':.<60}{M}")
print(f"{'Максимальная мощность пересечения множеств:':.<60}{len(res_1)}")
print(f"{'Искомое множество:':.<60}{res_1}")
print(f'{"Время поиска максимальной мощности пересечения множеств:":.<60}{res_2:.2f}')
