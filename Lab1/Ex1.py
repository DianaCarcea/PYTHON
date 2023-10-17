def cmmdc(a, b):
    while b:
        r = a % b
        a = b
        b = r

    return a


def cmmdc_vector(vector):
    val = cmmdc(vector[0], vector[1])
    for i in range(2, len(vector)):
        val = cmmdc(val, vector[i])

    return val


if __name__ == '__main__':

    vector = []
    n = int(input("Introduceti n:"))
    for i in range(0, n):
        x = int(input(f"Introduceti numarul cu indexul \'{i}\': "))
        vector.append(x)

    print(f"Cmmdc-ul lor este:", cmmdc_vector(vector))
