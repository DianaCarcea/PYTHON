def zip_lists(*lists):
    max_length = max(len(my_list) for my_list in lists)
    for my_list in lists:
        while len(my_list) < max_length:
            my_list.append(None)

    z = list(zip(*lists))
    print(z)


if __name__ == '__main__':
    print("Datele de la tastatura!")
    n = int(input("Introduceti numarul listelor:"))
    lists = []
    for i in range(n):
        my_list = input(f"Lista {i}: ").split()
        lists.append(my_list)

    zip_lists(*lists)

    print("\nDatele din cerinta:")
    zip_lists([1, 2, 3], [5, 6, 7], ["a", "b", "c"])
