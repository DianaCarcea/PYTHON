def is_prime(number):
    """Verificare primalitate"""
    if number == 0 or number == 1:
        return False
    d = 2
    while d*d <= number:
        if number % d == 0:
            return False
        d += 1
    return True


def get_prime_numbers(numbers):
    """Obtinerea listei cu numere prime"""
    prime_numbers = []

    for number in numbers:
        if is_prime(number):
            prime_numbers.append(number)

    return prime_numbers


if __name__ == '__main__':
    numbers = list(map(int, input("Introduceti numerele separate prin spatiu: ").split()))
    primes = get_prime_numbers(numbers)
    print(f"Numerele prime sunt: {primes}")