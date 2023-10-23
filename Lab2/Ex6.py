def elem_appear(*lists, nr_appearances):
    result = []

    all_elements = [elem for my_list in lists for elem in my_list]
    distinct_elements = set(all_elements)
    for element in distinct_elements:
        if all_elements.count(element) == nr_appearances:
            result.append(element)

    return result


if __name__ == '__main__':
    print("Datele de la tastatura!")
    n = int(input("Introduceti numarul listelor: "))
    lists = []
    for i in range(n):
        my_list = input(f"Lista {i}: ").split()
        lists.append(my_list)

    nr_appearances = int(input("Introduceti frecventa de cautare: "))

    print(elem_appear(*lists, nr_appearances=nr_appearances))

    print("\nDatele din cerinta:")
    print(elem_appear([1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"], nr_appearances=nr_appearances))
