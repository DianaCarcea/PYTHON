import sys

# Ex1
def intersect(a, b):
    """Intersectia dintre a si b"""
    return set(a) & set(b)


def union(a, b):
    """Reuniunea dintre a si b"""
    return set(a) | set(b)


def difference(a, b):
    """Diferenta dintre a si b"""
    return set(a)-set(b)


# Ex2
def count_chars(string):
    return {ch: string.count(ch) for ch in string}


#Ex3
def compare_lists(l1,l2):
    if not isinstance(l1, list) or not isinstance(l2, list):
        raise ValueError("Instantele nu sunt liste!")

    if len(l1) != len(l2):
        return False

    for val1, val2 in zip(l1, l2):
        if val1 != val2:
            return False

        if isinstance(val1, tuple) and isinstance(val2, tuple):
            if compare_tuples(val1, val2) is False:
                return False

        if isinstance(val1, list) and isinstance(val2, list):
            if compare_lists(val1, val2) is False:
                return False

        if isinstance(val1, set) and isinstance(val2, set):
            if compare_sets(val1, val2) is False:
                return False

        if isinstance(val1, dict) and isinstance(val2, dict):
            if compare_dictionaries(val1, val2) is False:
                return False

    return True


def compare_sets(s1, s2):
    if not isinstance(s1, set) or not isinstance(s2, set):
        raise ValueError("Instantele nu sunt seturi!")

    if len(s1) != len(s2):
        return False

    for val1, val2 in zip(s1, s2):
        if val1 != val2:
            return False

        if isinstance(val1, tuple) and isinstance(val2, tuple):
            if compare_tuples(val1, val2) is False:
                return False

        if isinstance(val1, list) and isinstance(val2, list):
            if compare_lists(val1, val2) is False:
                return False

        if isinstance(val1, set) and isinstance(val2, set):
            if compare_sets(val1, val2) is False:
                return False

        if isinstance(val1, dict) and isinstance(val2, dict):
            if compare_dictionaries(val1, val2) is False:
                return False

    return True


def compare_tuples(t1, t2):
    if not isinstance(t1, set) or not isinstance(t2, set):
        raise ValueError("Instantele nu sunt tuple!")

    if len(t1) != len(t2):
        return False

    for val1, val2 in zip(t1, t2):
        if val1 != val2:
            return False

        if isinstance(val1, tuple) and isinstance(val2, tuple):
            if compare_tuples(val1, val2) is False:
                return False

        if isinstance(val1, list) and isinstance(val2, list):
            if compare_lists(val1, val2) is False:
                return False

        if isinstance(val1, set) and isinstance(val2, set):
            if compare_sets(val1, val2) is False:
                return False

        if isinstance(val1, dict) and isinstance(val2, dict):
            if compare_dictionaries(val1, val2) is False:
                return False

    return True


def compare_dictionaries(d1, d2):
    if not isinstance(d1, dict) or not isinstance(d2, dict):
        raise ValueError("Instantele nu sunt dictionare!")

    if len(d1) != len(d2):
        return False

    d1 = dict(sorted(d1.items()))
    d2 = dict(sorted(d2.items()))

    for key1, val1 in d1.items():
        if key1 not in d2:
            return False

        val2 = d2[key1]
        if val1 != val2:
            return False

        if isinstance(val1, dict):
            if not compare_dictionaries(val1, val2):
                return False

        if isinstance(val1, list):
            if not compare_lists(val1, val2):
                return False

        if isinstance(val1, set):
            if not compare_lists(val1, val2):
                return False

        if isinstance(val1, tuple):
            if not compare_tuples(val1, val2):
                return False

    return True


#Ex4
def build_xml_element(tag, content, **key_value):
    all_key_val = ""
    for key, value in key_value.items():
        all_key_val = all_key_val + f'{key}="{value}" '
    if all_key_val:
        return f"<{tag} {all_key_val.rstrip()}>{content}</{tag}>"
    else:
        return f"<{tag}>{content}</{tag}>"


#Ex5
def validate_dict(rules, d):
    keys_rules = [rule[0] for rule in rules]
    for key_d, val in d.items():
        if key_d not in keys_rules:
            return False

    for rule in rules:
        key_rule, prefix, middle, suffix = rule

        if key_rule not in d:  #cheia nu se gaseste in dictionar => ok
            continue

        val = d[key_rule]

        # Valoarea nu incepe cu prefix
        if not val.startswith(prefix):
            return False

        # Tai prefixul
        val_fara_pref = val[len(prefix):]

        # Valoarea nu are sufix
        if not val_fara_pref.endswith(suffix):
            return False

        # Middle gol -> verific prefix si suffix
        if middle == "":
            if val.startswith(prefix) and val.endswith(suffix):
                continue
            else:
                return False

        # Prefix gol, verific daca val nu incepe cu middle
        if not prefix and val.startswith(middle):
            return False

        # Suffix gol, verific dacă val nu se termina cu middle
        if not suffix and val.endswith(middle):
            return False

        # Eliminăm prefix si sufix și verif dacă middle este in val
        middle_val = val[len(prefix):len(val)-len(suffix)]
        if middle not in middle_val:
            return False

    return True


#Ex6
def unique_dublicate(my_list):
    if not isinstance(my_list, list):
        raise TypeError("Tipul datei de intrare trebuie să fie lista!")

    a = {(elem, type(elem)) for elem in my_list}
    count = 0

    for elem, elem_type in a:
        aparitii = sum(1 for item in my_list if item == elem and type(item) == elem_type)
        if aparitii > 1:
            count += 1

    return len(a), count


#Ex7
def op_for_sets(*sets):
    d = {}
    sets_list = list(sets)
    for i in range(len(sets_list)):
        for j in range(i + 1, len(sets_list)):
            set1 = sets_list[i]
            set2 = sets_list[j]

            d[f"{set1} | {set2}"] = set1 | set2 if set1 | set2 else "empty set"
            d[f"{set1} & {set2}"] = set1 & set2 if set1 & set2 else "empty set"
            d[f"{set1} - {set2}"] = set1 - set2 if set1 - set2 else "empty set"
            d[f"{set2} - {set1}"] = set2 - set1 if set2 - set1 else "empty set"

    return d


#Ex8
def loop(mapping):

    if "start" not in mapping.keys():
        raise ValueError("Nu exista cheia 'start'!")

    result = []
    key = "start"
    while key in mapping and mapping[key] not in result:
        result.append(mapping[key])
        key = mapping[key]

    return result


#Ex9
def my_function(*args, **keyword_args):
    count = 0
    for val in args:
        if val in keyword_args.values():
            count += 1

    return count


if __name__ == '__main__':

    #Ex1
    print("\nEx1:")
    a = ["ana", "are", 2, "mere"]
    b = ["ion", "are", 3, "pere"]
    print(f"Intersectia dintre a si b: {intersect(a,b)}")
    print(f"Reuniunea dintre a si b: {union(a, b)}")
    print(f"Diferenta dintre a si b: {difference(a, b)}")
    print(f"Diferenta dintre b si a: {difference(b, a)}")


    #Ex2
    print("\nEx2:")
    print(count_chars("Ana has apples."))

    #Ex3
    print("\nEx3:")
    lista1 = [1, 2, 3]
    lista2 = [1, 2, 3]
    note1 = {"java": 8, "python": 10}
    note2 = {"java": 8, "python": 10}

    d1 = {"note": note1, "list": lista1, "nu": 0, "da": 1}
    d2 = {"note": note2, "list": lista2, "da": 1, "nu": 0}
    print(compare_dictionaries(d1, d2))

    print("----------------")

    string1 = "Ana are mere"
    string2 = "Ion are pere"
    d3 = {"note": note1, "str": string1, "list": lista1, "nu": 0, "da": 1}
    d4 = {"note": note2, "list": lista2, "str": string2, "da": 1, "nu": 0}
    print(compare_dictionaries(d3, d4))

    #Ex4
    print("\nEx4:")
    print(build_xml_element("a", "Hello there", href="http://python.org/", _class="my-link", id="someid"))
    print(build_xml_element("div", "Content goes here"))
    print(build_xml_element("input", "", type="text", placeholder="Enter something"))

    #Ex5
    print("\nEx5:")
    s = ("key1", "", "inside", ""), ("key2", "start", "middle", "winter")
    d = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
    print(validate_dict(s, d))

    #Ex6
    print("\nEx6:")
    my_list = [True, False, True, 1]
    print(unique_dublicate(my_list))

    #Ex7
    print("\nEx7:")
    result = op_for_sets({1, 2}, {2, 3})
    for key, value in result.items():
        print(f"{key}: {value}")

    #Ex8
    print("\nEx8:")
    print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))

    #Ex9
    print("\nEx9:")
    print(my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5))
