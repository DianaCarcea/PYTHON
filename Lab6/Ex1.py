import os
import sys


def read_file(path_file):
    try:
        with open(path_file, 'r') as file:
            buffer = file.read()
        return buffer
    except Exception as e:
        print(f"Eroare la citirea fisierului {path_file}: {e}")


def display_info(path_file):
    try:
        buffer = read_file(path_file)
        print(f"{buffer}\n")

    except Exception as e:
        print(f"Eroare la afisarea info din fisierul {path_file}: {e}")


def iteration_dir(directory, extension):
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directorul {directory} nu a fost găsit!")

        if not os.path.isdir(directory):
            raise NotADirectoryError(f"{directory} nu este director!")

        if len(extension) < 2:
            raise ValueError(f"Extensie incorectă: {extension}")

        files_with_extension = [f for f in os.listdir(directory) if f.endswith(extension)]
        for file_name in files_with_extension:
            file_path = os.path.join(directory, file_name)
            print(f"- {file_name}")
            display_info(file_path)

        for sub_dir in os.listdir(directory):  # recursive
            sub_dir_path = os.path.join(directory, sub_dir)
            if os.path.isdir(sub_dir_path):
                iteration_dir(sub_dir_path, extension)

        return files_with_extension

    except Exception as e:
        print(f"Error: {e}")
        return []


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Linie de tipul: python Ex1.py <director> <extensie>")
        sys.exit(1)

    director = sys.argv[1]
    extensie = sys.argv[2]
    iteration_dir(director, extensie)

