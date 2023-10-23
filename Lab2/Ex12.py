def group_by_rhyme(lists_of_words):
    result = []
    processed_words = []

    for word in lists_of_words:
        if word not in processed_words:
            rhymes = [my_word for my_word in lists_of_words if my_word[-2:] == word[-2:]]
            result.append(rhymes)
            for r_word in rhymes:  # Cuvinte procesate
                processed_words.append(r_word)

    # Elimin cuvintele care au rima
    for word in processed_words:
        lists_of_words.remove(word)

    # Adaug cuvintele care au ramas fara rima
    for word in lists_of_words:
        result.append([word])

    print(result)


if __name__ == '__main__':
    print("Datele de la tastatura!")
    lists_of_words = list(input("Inserati lista de cuvinte: ").split())
    group_by_rhyme(lists_of_words)

    print("\nDatele din cerinta:")
    group_by_rhyme(["ana", "banana", "carte", "arme", "parte"])
