def read_tuples():
    n = int(input("Inserati numarul de tuple:"))
    lists = []
    for i in range(n):
        print(f"Tuplul {i+1}:")
        first_elem = input("1st element: ")
        second_elem = input("2nd element: ")
        lists.append((first_elem, second_elem))
    return lists


def order_3rd_char(lists):
    return sorted(lists, key=lambda x: x[1][2] if len(x[1]) > 2 else '')  #Ordonare dupa char al 3 din elem 2


if __name__ == '__main__':

    print("Datele de la tastatura!")
    lists = read_tuples()
    lists = order_3rd_char(lists)
    print(lists)

    print("\nDatele din cerinta:")
    print(order_3rd_char([("abc", "bcd"), ("abc", "zza")]))
