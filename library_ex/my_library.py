import os


class Library:
    def __init__(self, books_dir):
        self.book_dir = books_dir
        pass  # TODO

    def list_books(self):
        """
        List book id's
        :return:
        """
        files = os.listdir(self.books_dir)
        return files

    @staticmethod
    def search(word, book_id=None):
        """
        Search a word in a book
        :param word: str. The word to search
        :param book_id: Optional argument. the book id to search in
        :return: print list of book id's in which the word exist
        """
        my_file = open(book_id)
        if word in my_file.read():
            print("word found")
        else:
            print("word not found")
        pass  # TODO

    search('Project', '84-0.txt')

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
