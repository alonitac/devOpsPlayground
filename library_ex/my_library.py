import os


class Library:
    def __init__(self, books_dir):
        pass  # TODO

    def list_books(self):
        """
        List book id's
        :return:
        """
        files = os.listdir(self.books_dir)
        return files

    def search(self, word, book_id=None):
        """
        Search a word in a book
        :param word: str. The word to search
        :param book_id: Optional argument. the book id to search in
        :return: print list of book id's in which the word exist
        """
        pass  # TODO

    def get_book_name(self, book_id):
        """
        :param book_id:
        :return: The book title
        """
        pass  # TODO

    def get_author(self, book_id):
        """
        :param book_id:
        :return: The book author
        """
        pass  # TODO