def word_counter(text):
    text = text.split()
    return len(text)


if __name__ == '__main__':
    text = input("Introduceti textul: ")
    print(f"Textul contine: {word_counter(text)} cuvinte")