from random import randint

def array_5_5():
    array = [[randint(10, 99) for i in range(5)] for j in range(5)]
    [print(*i) for i in array]
    print()

    min_alem = array[0][0]
    min_i = 0
    min_j = 0
    for i in range(5):
        for j in range(5):
            if array[i][j] < min_alem:
                min_i, min_j = i, j
                min_alem = array[i][j]
    print(f"i_min = {min_i}")
    print(f"j_min = {min_j}")
    print(f"min_alem = {min_alem}")

array_5_5()