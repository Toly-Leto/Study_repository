import random

def get_even_number(lst):
    return len([i for i in lst if not i % 2])

def factorial(num):
    if num < 1: return 1
    return num * factorial(num - 1)

def fib(num):
    if num < 2: return num
    return fib(num -1) + fib(num - 2)


def make_lst(num):
    return [random.randint(0,  1000) for i in range(num)]

n = int(input('Введите число N: '))
lst = make_lst(n)

print(f'Число чётных числе в списке размером N = {get_even_number(lst)}')
print(f'Факториал числа N = {factorial(n)}')
print(f'Число Фибоначчи под номером N = {fib(n)}')