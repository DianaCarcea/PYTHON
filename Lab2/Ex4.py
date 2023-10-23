def valid_musical_notes(musical_notes):
    notes = "do", "re", "mi", "fa", "sol", "la", "si"
    for note in musical_notes:
        if note not in notes:
            print(f"'{note}' nu este o nota muzicala valida")
            return 0
    return 1


def compose(musical_notes, moves, start_pos):
    song = []
    current_pos = start_pos
    song.append(musical_notes[current_pos])
    for move in moves:
        current_pos = (current_pos + move) % len(musical_notes)
        song.append(musical_notes[current_pos])

    print(f"Melodia rezultata este: {song}")
    return song


if __name__ == '__main__':
    musical_notes = input("Intoduceti notele muzicale: ").split()
    while valid_musical_notes(musical_notes) == 0:
        musical_notes = input("Intoduceti notele muzicale: ").split()

    moves = list(map(int, input("Intoduceti miscarile notelor: ").split()))
    start_pos = int(input("Intoduceti pozitia de start: "))

    while not(0 <= start_pos < len(musical_notes)):
        print(f"Pozitia '{start_pos}' nu corespunde cu lista notelor")
        start_pos = int(input("Intoduceti pozitia de start: "))

    compose(musical_notes, moves, start_pos)
