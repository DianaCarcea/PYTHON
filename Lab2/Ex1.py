# Elementul de pe pozitia n in sirul lui Fibbonacci
def fib_recursive(n):
    """
    Elementul de pe pozitia n in sirul lui Fibbonacci
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


if __name__ == '__main__':
    n = int(input("Introduceti n:"))
    for i in range(1, n+1):
        print(fib_recursive(i), end=' ')

