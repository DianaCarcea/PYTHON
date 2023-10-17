def nr_vowels(string):
    vowels = "aeiouAEIOU"
    counter = 0
    for i in range(0, len(string)):
        if string[i] in vowels:
            counter = counter + 1

    return counter


if __name__ == '__main__':
    string = input("Inserati sirul:")
    nr_vowels_string = nr_vowels(string)
    print(f"Numarul de vocale ale sirului \'{string}\' este: ", nr_vowels_string)

