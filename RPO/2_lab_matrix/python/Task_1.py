from random import randint

def list_of_numbers():
    N = int(input("Input N: "))
    list_rand_nums = [randint(-10, 10) for _ in range(N)]

    positive = [i for i in list_rand_nums if i > 0]
    arithmetic_mean = sum(positive)/len(positive)

    print(f'{"List of numbers:":<30}{list_rand_nums}')
    print(f'{"List of positive numbers:":<30}{positive}')
    print(f'{"arithmetic mean:":<30}{arithmetic_mean}')


list_of_numbers()