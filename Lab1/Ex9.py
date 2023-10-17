def most_common_character(text):
    lower_text = text.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter_frequency = [0] * len(alphabet)

    for letter in lower_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            letter_frequency[index] += 1

    index_max = letter_frequency.index(max(letter_frequency))
    if max(letter_frequency) != 0:
        return (alphabet[index_max], max(letter_frequency))


if __name__ == '__main__':
    text = input("Introduceti textul: ")
    letter, freq = most_common_character(text)
    print(f"Caracterul cel mai comun este: {letter} si apare de: {freq} ori")
