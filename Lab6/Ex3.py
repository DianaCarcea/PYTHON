import os
import sys


def iteration_dir(director):
    size = 0
    try:

        if not os.path.exists(director):
            raise FileNotFoundError(f"Directorul {director} nu a fost gasit!")

        if not os.path.isdir(director):
            raise NotADirectoryError(f"{director} nu este director!")

        for file_name in os.listdir(director):
            full_path = os.path.join(director, file_name)
            try:
                file_size = os.path.getsize(full_path)  # recursive
                size += file_size
                print(f"- {file_name} ({file_size} bytes)")

                if os.path.isdir(full_path):
                    size += iteration_dir(full_path)

            except (PermissionError, FileNotFoundError) as e:
                print(f"Eroare la accesarea fișierului '{full_path}': {e}")

        return size

    except Exception as e:
        print(f"Error: {e}")
        return 0


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Linie de tipul: python Ex3.py <path_director>")
        sys.exit(1)

    path_dir = sys.argv[1]
    size = iteration_dir(path_dir)
    print(f"Dimensiunea totala este: {size} bytes!")
