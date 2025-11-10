def f(num):
    print(num)
    if num == 0:
        print('Мы на дне, возвращаемся!')
        return
    else:
        f(num - 1)
        print(num)
    return

print(f(5))