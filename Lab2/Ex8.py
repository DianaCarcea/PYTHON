# false - caractere cu cod ascii nedivizibile cu x
# true - caractere cu cod ascii divizibile cu x
def char_div_ascii(x=1, my_list=None, flag=True):
    result = []
    if my_list == None:
        return []

    for string in my_list:
        elem = []
        for char in string:
            if flag == True and ord(char) % x == 0:
                elem.append(char)
            elif flag == False and ord(char) % x != 0:
                elem.append(char)
        if elem:
            result.append(elem)

    return result


if __name__ == '__main__':
    print("Datele de la tastatura!")
    x = int(input("Inserati x: "))
    my_list = list(input("Inserati lista: ").split())
    print(f"\033[93mDoriti caractelele cu codul Ascii care se divid la {x}? ('False' sau 'True')\033[0m")
    flag_input = input("Flag: ").strip().lower()
    while flag_input not in ("true", "false"):
        print(f"\033[93mAlegeti: 'False' sau 'True'\033[0m")
        flag_input = input("Flag: ").strip().lower()

    flag = flag_input == "true"

    print(char_div_ascii(x=x, my_list=my_list, flag=flag))

    print("\nDatele implicite!")
    print(char_div_ascii(my_list=my_list))


