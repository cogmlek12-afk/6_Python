from models import Book, BookNotFoundError

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_all_books(self):
        for book in self.books:
            print(book)
            print("=" * 3)

    def search_available_books(self, keyword):
        for book in self.books:
            if not book.is_borrowed:
                if keyword in book.title or keyword in book.author:
                    print(book)

    def show_authors(self):
        authors = set()

        for book in self.books:
            authors.add(book.author)

        for author in authors:
            print(author)

    def delete_book(self, isbn):
        found = False

        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                found = True
                print("책이 삭제되었습니다.")

        if not found:
                raise BookNotFoundError("해당 ISBN의 책을 찾을 수 없습니다.")
            
    def borrow_book(self, isbn):
        found = False 

        for book in self.books:
            if book.isbn == isbn:
                book.borrow()
                found = True
                print("책이 대출되었습니다.")

        if not found:
            raise BookNotFoundError("해당 ISBN의 책을 찾을 수 없습니다.")

    def return_book(self, isbn):
        found = False

        for book in self.books:
            if book.isbn == isbn:
                book.return_book()
                found = True 

        if not found:
            raise BookNotFoundError("해당 ISBN의 책을 찾을 수 없습니다.")


