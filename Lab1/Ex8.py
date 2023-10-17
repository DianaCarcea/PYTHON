def decimal_to_binary(decimal_number):
    binary_number = ""
    if decimal_number == 0:
        return "0"
    while decimal_number != 0:
        if decimal_number % 2 == 0:
            binary_number = "0" + binary_number
        else:
             binary_number = "1" + binary_number

        decimal_number //= 2

    return binary_number


def nr1_of_binary(binary_number):

    str_binary_number = str(binary_number)
    counter = 0
    i = 0
    while len(str_binary_number) > i:
        if str_binary_number[i] == "1":
            counter += 1
        i += 1

    return counter


if __name__ == '__main__':
    decimal_number = int(input("Introduceti numarul: "))
    binary_number = decimal_to_binary(decimal_number)
    print(f"Numarul in binar este: ", binary_number)
    print(f"Numarul de 1 este: ", nr1_of_binary(binary_number))
