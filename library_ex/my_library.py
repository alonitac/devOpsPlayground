import os


class BookNotFound(Exception):
    pass


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
        :param book_id: Optional argument, list. the book id to search in
        :return: print list of book id's in which the word exist
        """
        pass  # TODO

    def get_book_name(self, book_id):
        """
        :param book_id:
        :return: The book title
        """
        if book_id in self.list_books():
            # book_file = open(book_id)
            # book_lines = book_file.readlines()
            for line in open(f'{self.books_dir}/{book_id}', mode='r'):
                # Adham
                # if line[:7] == 'Title: ':
                #     return line[7:]

                # Abeer
                # for word in line.split():
                #     if 'Title' in word:
                #         return line[7:]

                # Ebraheem
                # p = line.split(':')
                # if p[0] == 'Title':
                #     return p[1]

                # Elia
                if line.startswith('Title:'):
                    return line[7:]
            return 'Bad book format'
        else:
            raise BookNotFound(f'The book {book_id} was not found in {self.books_dir}. Available book are {self.list_books()}')

    def get_author(self, book_id):
        """
        :param book_id:
        :return: The book author
        """
        pass  # TODO


lib = Library('books')
print(lib.get_book_name('pggggg43453.txt'))
