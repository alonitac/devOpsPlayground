import os
import books

class Library:
    def __init__(self, books_dir):
        self.books_dir = books_dir

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
        my_file = open(book_id)
        file_lines = my_file.readlines()
        for line in file_lines:
            if line[:7] == 'Author:':
                print(line[7:])


    def get_author(self, book_id):
        """
        :param book_id:
        :return: The book author
        """
        my_file = open(book_id)
        file_lines = my_file.readlines()
        for line in file_lines:
            if line[:7] == 'Author:':
                print(line[7:])
        my_file.close()

lib = Library('books')
lib.list_books()
lib.get_author('books/1342-0.txt')



