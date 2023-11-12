import time


class LibraryItem:

    def __init__(self, ID, author, title, year_release, language):
        self._checked_out = False
        self._ID = ID
        self._author = author
        self._title = title
        self._year_release = self._validate_year(year_release)
        self._language = self._validate_language(language)

    def check_out(self):
        if self._checked_out:
            print("Acest obiect este deja împrumutat.")
        else:
            print(f"Ai imprumutat {self._title} de {self._author}.")
            self._checked_out = True

    def return_item(self):
        if not self._checked_out:
            print("Acest obiect nu este împrumutat.")
        else:
            print(f"{self._title} de {self._author} a fost returnat.")
            self._checked_out = False

    VALID_LANGUAGES = ["Română", "Engleză", "Franceză", "Germană", "Spaniolă", "Italiană"]

    def _validate_language(self, language):
        if language not in self.VALID_LANGUAGES:
            raise ValueError(f"Limbă nevalidă. Limbile valide sunt: {', '.join(self.VALID_LANGUAGES)}.")
        return language

    def _validate_year(self, year):
        current_year = 2023
        if not isinstance(year, int) or year < 0 or year > current_year:
            raise ValueError(
                "Anul aparitiei trebuie să fie un număr întreg pozitiv mai mic sau egal cu anul curent.")
        return year

    def display_info(self):
        print(f"Status: {'Checked Out' if self._checked_out else 'Available'}\n"
              f"Item ID: {self._ID}\n"
              f"Title: {self._title}\n"
              f"Author: {self._author}\n"
              f"Release year: {self._year_release}")


class Book(LibraryItem):
    def __init__(self, ID, title, author, year_release, language, nr_pages, genre, isbn):
        super().__init__(ID, title, author, year_release, language)
        self._nr_pages = self._validate_pages(nr_pages)
        self._genre = self._validate_genre(genre)
        self._isbn = isbn

    def _validate_pages(self, nr_pages):
        if not isinstance(nr_pages, int) or nr_pages <= 0:
            raise ValueError("Numărul de pagini trebuie să fie un număr întreg pozitiv.")
        return nr_pages

    VALID_GENRES = ["Ficțiune", "Non-ficțiune", "SF", "Mister", "Poezie", "Biografie", "Istorie", "Fantasy", "Poveste"]

    def _validate_genre(self, genre):
        if genre not in self.VALID_GENRES:
            raise ValueError(f"Gen nevalid. Genurile valide sunt: {', '.join(self.VALID_GENRES)}.")
        return genre

    def set_genre(self, new_genre):
        self._genre = new_genre
        print(f"Genul cărții '{self._title}' a fost actualizat la '{new_genre}'.")

    def display_detailed_info(self):
        super().display_info()
        print(f"Number of Pages: {self._nr_pages}")
        print(f"Genre: {self._genre}")
        print(f"ISBN: {self._isbn}")
        print(f"Language: {self._language}")


class DVD(LibraryItem):
    def __init__(self, ID, title, director, year_release, language, duration):
        super().__init__(ID, director, title, year_release, language)
        self._duration = self._validate_duration(duration)
        self._start_time = None

    def _validate_duration(self, duration):
        if not isinstance(duration, int) or duration <= 0:
            raise ValueError("Durata trebuie să fie un număr întreg pozitiv.")
        return duration

    def play(self):
        if self._checked_out:
            if not self._start_time:
                print(f"{self._title} se redă acum.")
                self._start_time = time.time()
                time.sleep(2)  # 2 secunde de redare
            else:
                print(f"{self._title} este deja în redare.")
        else:
            print(f"{self._title} nu poate fi redat. Este necesar să fie împrumutat pentru a începe redarea.")

    def stop(self):
        if self._start_time:
            elapsed_time = time.time() - self._start_time
            print(f"{self._title} s-a oprit. Timpul scurs: {elapsed_time:.2f} secunde.")
            self._start_time = None
        else:
            print(f"{self._title} nu este în redare.")

    def display_detailed_info(self):
        super().display_info()
        print(f"Duration: {self._duration} minutes")
        print(f"Director: {self._author}")


class Magazine(LibraryItem):
    def __init__(self, ID, title, publisher, year_release, language, publication_month, nr_pages):
        super().__init__(ID, title, publisher, year_release, language)
        self._publication_month = self._validate_month(publication_month)
        self._nr_pages = self._validate_pages(nr_pages)
        self._articles = []

    def _validate_pages(self, nr_pages):
        if not isinstance(nr_pages, int) or nr_pages <= 0:
            raise ValueError("Numărul de pagini trebuie să fie un număr întreg pozitiv.")
        return nr_pages

    def _validate_month(self, month):
        luni_valide = ["ianuarie", "februarie", "martie", "aprilie", "mai", "iunie", "iulie", "august", "septembrie",
                       "octombrie", "noiembrie", "decembrie"]
        luna_cautata = month.lower()
        if luna_cautata not in luni_valide:
            raise ValueError("Luna de publicare nu este validă.")
        return luna_cautata.capitalize()

    def add_article(self, article_title, author):
        article = {"title": article_title, "author": author}
        self._articles.append(article)
        print(f"Articol adăugat cu succes: '{article_title}' de către {author}.")

    def display_articles(self):
        if self._articles:
            print(f"Articole în revistă '{self._title}':")
            for article in self._articles:
                print(f"- {article['title']} de {article['author']}")
        else:
            print(f"Nu există articole în revistă '{self._title}'.")

    def display_detailed_info(self):
        super().display_info()
        print(f"Publication month: {self._publication_month}\n"
              f"Numbers of Pages: {self._nr_pages}\n"
              f"Numbers of Articles: {len(self._articles)}")


if __name__ == '__main__':
    print("---------BOOK---------")
    book1 = Book("B1", "Harap-Alb", "Ion Creanga", 1877, "Română", 150, "Poveste", "978-973-37-1522-3")
    book1.display_detailed_info()

    print("\n---------DVD---------")
    dvd1 = DVD("D1", "Titanic", "James Cameron", 1997, "Engleză", 194)
    dvd1.display_detailed_info()
    dvd1.check_out()
    dvd1.play()
    dvd1.stop()
    dvd1.return_item()

    print("\n---------MAGAZINE---------")
    magazine1 = Magazine("M1", "Science", "American Association for the Advancement of Science", 2023, "Engleză", "Mai", 80)
    magazine1.check_out()

    magazine1.add_article("The Future of Space Exploration", "Dr. Astronomer")
    magazine1.add_article("Advancements in Artificial Intelligence", "Tech Guru")

    magazine1.display_detailed_info()
    magazine1.display_articles()

    magazine1.return_item()
