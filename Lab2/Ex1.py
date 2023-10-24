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


def fib_list(n):
    """
    Return a list of the first n numbers in the Fibonacci string
    """
    if n < 0:
        print(f"\033[91mValoarea lui n nu poate fi negativa!\033[0m")
        exit(-1)

    if n == 0:
        print(f"\033[91mValoarea lui n nu poate fi zero!\033[0m")
        exit(-1)

    return [fib_recursive(i) for i in range(1, n+1)]


if __name__ == '__main__':
    n = int(input("Introduceti n: "))
    print(fib_list(n))
