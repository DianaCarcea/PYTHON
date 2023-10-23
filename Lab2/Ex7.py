def is_palindrome(number):
    str_number = str(number)
    n = len(str_number)
    for i in range(0, n//2):
        if str_number[i] != str_number[n-i-1]:
            return False
    return True


def info_palindromes(my_numbers):
    counter = 0
    palindromes = []
    for number in my_numbers:
        if is_palindrome(number):
            counter += 1
            palindromes.append(number)

    if counter == 0:
        print(f"\033[91mNu exista numere de tip palindrom!\033[0m")
        exit(-1)

    return counter, max(palindromes)


if __name__ == '__main__':
    numbers = list(map(int, input("Inserati lista de numere: ").split()))
    count, maxim_palindrome = info_palindromes(numbers)
    print(f"Numar palindroame: {count}")
    print(f"Palindromul cel mai mare: {maxim_palindrome}")