def read_matrix(matrix):
    dim_matrix = int(input("Introduceti dimensiunea matricei: "))

    print(f"Introduceti cate {dim_matrix} numere separate de spatiu pe fiecare rand!")
    for i in range(dim_matrix):
        row = input(f"Randul {i}: ").split()
        while dim_matrix != len(row):
            print(f"Nu ati introdus exact {dim_matrix} numere pe rand.")
            row = input(f"Randul {i}: ").split()
        matrix.append(row)


#modelul spirala
def print_matrix(matrix):
    dim_matrix = len(matrix)
    if dim_matrix == 0:
        return

    strat = 0

    while strat*2 <= dim_matrix:    #2*2<=4 (matricea de 4 are maxim 2 straturi)
        #In dreapta
        for col in range(strat, dim_matrix-strat):  #col in (0,2)
            print(matrix[strat][col], end=' ')
        #In jos
        for line in range(strat+1, dim_matrix-strat):
            print(matrix[line][dim_matrix-strat-1], end=' ')
        #In stanga
        if strat < dim_matrix - strat - 1:  # Pentru a nu merge inapoi pe acelasi rând 0<4-0-1=3
            for col in range(dim_matrix - strat - 2, strat - 1, -1):
                print(matrix[dim_matrix - strat - 1][col], end=' ')
        #In sus
        if strat < dim_matrix - strat - 1:  # Pentru a nu merge inapoi pe aceeasi coloane 0<4-0-1=3
            for line in range(dim_matrix - strat - 2, strat, -1):   
                print(matrix[line][strat], end=' ')

        strat += 1


if __name__ == '__main__':
    matrix = []
    read_matrix(matrix)
    print("Matricea citită este:")
    print_matrix(matrix)

