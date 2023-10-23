def intersect(a, b):
    """Intersectia dintre a si b"""
    return list(set(a) & set(b))


def union(a, b):
    """Reuniunea dintre a si b"""
    return list(set(a) | set(b))


def difference(a, b):
    """Diferenta dintre a si b"""
    return list(set(a) - set(b))


if __name__ == '__main__':
    a = input("Introduceti lista a: ").split()
    b = input("Introduceti lista b: ").split()
    print(f"Intersectia dintre a si b: {intersect(a,b)}")
    print(f"Reuniunea dintre a si b: {union(a, b)}")
    print(f"Diferenta dintre a si b: {difference(a, b)}")
    print(f"Diferenta dintre b si a: {difference(b, a)}")