def read_matrix(matrix):
    print("Introduceti dimensiunea matricei: ")
    n = int(input("n = "))
    m = int(input("m = "))

    print(f"Introduceti cate '{n}' randuri a cate '{m}' coloana!")

    for i in range(n):
        row = input(f"Randul {i}: ").split()
        while m != len(row):
            print(f"Nu ati introdus exact {m} numere pe rand.")
            row = input(f"Randul {i}: ").split()
        matrix.append(row)


def main_diag(matrix):
    result = [elem[:] for elem in matrix]
    length_diag = min(len(matrix), len(matrix[0]))  # minim dintre rand si col
    for i in range(length_diag):
        result[i][i] = 0
    return result


def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end=" ")
        print()


if __name__ == '__main__':
    matrix = []
    read_matrix(matrix)
    result = main_diag(matrix)
    print_matrix(result)
