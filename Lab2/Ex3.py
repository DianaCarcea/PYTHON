def intersect(a, b):
    """Intersectia dintre a si b"""
    return [elem for elem in a if elem in b]


def union(a, b):
    """Reuniunea dintre a si b"""
    result = a.copy()
    for elem in b:
        if elem not in result:
            result.append(elem)
    return result


def difference(a, b):
    """Diferenta dintre a si b"""
    return [elem for elem in a if elem not in b]


if __name__ == '__main__':
    a = input("Introduceti lista a: ").split()
    b = input("Introduceti lista b: ").split()
    print(f"Intersectia dintre a si b: {intersect(a,b)}")
    print(f"Reuniunea dintre a si b: {union(a, b)}")
    print(f"Diferenta dintre a si b: {difference(a, b)}")
    print(f"Diferenta dintre b si a: {difference(b, a)}")