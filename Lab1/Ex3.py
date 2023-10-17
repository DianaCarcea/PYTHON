def nr_occurrences_sting(first_string,second_string):

    counter = 0
    first_occurrences = second_string.find(first_string)
    while first_occurrences != -1:
        counter = counter+1
        first_occurrences = second_string.find(first_string, first_occurrences+1)

    return counter


if __name__ == '__main__':
    first_string = input("Inserati primul string: ")
    second_string = input("Inserati al doilea string: ")
    nr_aparitii = nr_occurrences_sting(first_string, second_string)
    print(f"Primul sir se gaseste in cel de-al doile de \'{nr_aparitii}\' ori")