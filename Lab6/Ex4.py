import os
import sys


def print_dir(extension_dir, no_extension_count):
    if extension_dir is not None:
        print("Numărul de fișiere pe fiecare extensie:")
        for extension, count in extension_dir.items():
            print(f"{extension}: {count} fișiere")

        if no_extension_count > 0:
            print(f"Fără extensie: {no_extension_count} fișiere")

    else:
        print("Nu s-a putut număra fișierele pe extensii.")


def iteration_dir(director, extension_dir=None, no_extension_count=0):
    if extension_dir is None:
        extension_dir = {}

    try:

        if not os.path.exists(director):
            raise FileNotFoundError(f"Directorul {director} nu a fost gasit!")

        if not os.path.isdir(director):
            raise NotADirectoryError(f"{director} nu este director!")

        for file_name in os.listdir(director):
            full_path = os.path.join(director, file_name)

            if os.path.isdir(full_path):  # recursive
                iteration_dir(full_path, extension_dir, no_extension_count)
            else:
                _, file_extension = os.path.splitext(file_name)
                file_extension = file_extension.lower()

                if file_extension:
                    if file_extension not in extension_dir:
                        extension_dir[file_extension] = 1
                    else:
                        extension_dir[file_extension] += 1
                else:
                    no_extension_count += 1

    except PermissionError:
        print(f"Eroare: Permisiune refuzată pentru directorul: {director}")

    except Exception as e:
        print(f"Error: {e}")
        return 0

    return extension_dir, no_extension_count


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Linie de tipul: python Ex4.py <path_director>")
        sys.exit(1)

    path_dir = sys.argv[1]
    extension_dir, no_extension_count = iteration_dir(path_dir)
    print_dir(extension_dir, no_extension_count)

