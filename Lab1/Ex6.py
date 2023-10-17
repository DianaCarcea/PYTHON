#12321
def is_palindrome(number):
    str_number = str(number)
    n = len(str_number)
    for i in range(0, n//2):
        if str_number[i] != str_number[n-i-1]:
            return False

    return True


if __name__ == '__main__':
    number = int(input("Inserati numarul: "))
    if is_palindrome(number):
        print(f"Numarul {number} este palindrom.")
    else:
        print(f"Numarul {number} nu este palindrom.")