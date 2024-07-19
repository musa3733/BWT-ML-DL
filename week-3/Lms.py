# Library Management System/LMS.py

class Book:
    def __init__(self, title, author, pages):
        self._title = title
        self._author = author
        self._pages = pages

    # Getter and Setter for title
    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    # Getter and Setter for author
    def get_author(self):
        return self._author

    def set_author(self, author):
        self._author = author

    # Getter and Setter for pages
    def get_pages(self):
        return self._pages

    def set_pages(self, pages):
        if pages < 0:
            raise ValueError("Number of pages cannot be negative.")
        self._pages = pages

    # Method to calculate reading time
    @classmethod
    def reading_time(cls, pages, speed=250):
        """
        Calculate the reading time based on an assumed reading speed.

        :param pages: Number of pages in the book
        :param speed: Reading speed (words per minute), default is 250 wpm
        :return: Estimated reading time in minutes
        """
        words_per_page = 300  # Assume an average of 300 words per page
        total_words = pages * words_per_page
        time_minutes = total_words / speed
        return time_minutes

    def __str__(self):
        return f"Book: {self._title}, Author: {self._author}, Pages: {self._pages}"


class Ebook(Book):
    def __init__(self, title, author, pages, format):
        super().__init__(title, author, pages)
        self._format = format

    def get_format(self):
        return self._format

    def set_format(self, format):
        self._format = format

    def __str__(self):
        return f"Ebook: {self._title}, Author: {self._author}, Pages: {self._pages}, Format: {self._format}"


# Demonstration
if __name__ == "__main__":
    try:
        # Create an instance of Book
        my_book = Book("1984", "George Orwell", 328)

        # Use getter methods
        print(my_book.get_title())  # Output: 1984
        print(my_book.get_author())  # Output: George Orwell
        print(my_book.get_pages())  # Output: 328

        # Use setter methods
        my_book.set_title("Animal Farm")
        my_book.set_author("George Orwell")
        my_book.set_pages(112)

        print(my_book)  # Output: Book: Animal Farm, Author: George Orwell, Pages: 112

        # Calculate reading time
        reading_time = Book.reading_time(my_book.get_pages())
        print(f"Estimated reading time: {reading_time:.2f} minutes")

        # Create an instance of Ebook
        my_ebook = Ebook("The Great Gatsby", "F. Scott Fitzgerald", 180, "PDF")

        # Use getter and setter methods for Ebook
        print(my_ebook.get_format())  # Output: PDF
        my_ebook.set_format("EPUB")

        print(my_ebook)  # Output: Ebook: The Great Gatsby, Author: F. Scott Fitzgerald, Pages: 180, Format: EPUB

    except Exception as e:
        print(f"An error occurred: {e}")
