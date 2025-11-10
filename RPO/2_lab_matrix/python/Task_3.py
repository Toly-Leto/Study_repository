from random import randint

def transpon():
    N = int(input("Введите N: "))
    mtrx = [[randint(10, 99) for i in range(N)] for j in range(N)]
    for line in mtrx: print(*line)
    print()

    transposed = zip(*mtrx)
    for line in transposed: print(*line)

transpon()