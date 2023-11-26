import os


def rename_files(path_dir):
    try:
        if not os.path.exists(path_dir):
            raise FileNotFoundError(f"Directorul {path_dir} nu a fost gasit!")

        all_files = os.listdir(path_dir)
        index = 1

        for file in all_files:
            path_file = os.path.join(path_dir, file)
            if os.path.isdir(path_file):
                rename_files(path_file)  # recursive
            else:
                file_name, extension = os.path.splitext(file)
                new_file = f"{file_name}{index}{extension}"
                path_new_file = os.path.join(path_dir, new_file)

                try:
                    os.rename(path_file, path_new_file)
                    print(f"{file} -> {new_file}")
                    index += 1

                except PermissionError:
                    print(f"Eroare de permisiune: Nu se poate redenumi {file}!")
                except FileNotFoundError:
                    print(f"Fisierul: {file} nu a fost gasit pentru redenumire!")

    except FileNotFoundError as e:
        print(f"Eroare: {e}")

    except Exception as e:
        print(f"A apărut o eroare neașteptată: {e}")


if __name__ == '__main__':
    directory_path = "C://Users//diana//OneDrive//Desktop//Ex2"
    rename_files(directory_path)
    