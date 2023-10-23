def read_matrix(matrix):
    print("Introduceti dimensiunea matricei: ")
    n = int(input("n = "))
    m = int(input("m = "))

    print(f"Introduceti cate '{n}' randuri a cate '{m}' coloana!")

    for i in range(n):
        row = list(map(int,input(f"Randul {i}: ").split()))
        while m != len(row):
            print(f"Nu ati introdus exact {m} numere pe rand.")
            row = list(map(int, input(f"Randul {i}: ").split()))
        matrix.append(row)


def find_bad_places(matrix):
    bad_places = []
    nr_row = len(matrix)
    nr_col = len(matrix[0])
    for col in range(nr_col):
        for row in range(1, nr_row):
            for k in range(row):
                if matrix[row][col] <= matrix[k][col]:
                    bad_places.append((row, col))
                    break

    return bad_places


if __name__ == '__main__':
    matrix = []
    read_matrix(matrix)
    print(find_bad_places(matrix))