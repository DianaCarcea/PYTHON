# AnaAreMere -> ana_are_mere

def convertor(string):
    new_string = ""

    if 'A' <= string[0] <= 'Z':
        new_string += string[0].lower()

    for i in range(1, len(string)):
        if 'A' <= string[i] <= 'Z':
            new_string += '_'
            new_string += string[i].lower()
        else:
            new_string += string[i]

    return new_string


if __name__ == '__main__':
    string = input("Inserati sirul: ")
    string_without_spaces = string.replace(" ", "")
    print(f"Sirul in format lowercase_with_underscores: ", convertor(string_without_spaces))
