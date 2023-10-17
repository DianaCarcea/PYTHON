def extract_first_number(text):
    number = ""
    n = len(text)
    numbers = "0123456789"
    i = 0
    while i < n:
        if text[i] in numbers:
            while i < n and text[i] in numbers:
                number += text[i]
                i += 1
            break
        i += 1

    return number

if __name__ == '__main__':
    text = input("Inserati textul: ")
    number = extract_first_number(text)
    print(f"Primul numar din text este: {number}.")