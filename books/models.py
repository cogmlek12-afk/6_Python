class AlreadyBorrowedError(Exception):
    pass
class BookNotFoundError(Exception):
    pass

class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            raise AlreadyBorrowedError("이미 대출 중인 책입니다.")

        self.is_borrowed = True

    def return_book(self):
        self.is_borrowed = False

    def __str__(self):
        status = "대출 중" if self.is_borrowed else "대출 가능"
        return (
        f"ISBN : {self.isbn}\n"
        f"제목 : {self.title}\n"
        f"저자 : {self.author}\n"
        f"대출 상태 : {status}"
    )

class EBook(Book):
    def __init__(self, isbn, title, author, file_format, file_size):
        super().__init__(isbn, title, author)
        self.file_format = file_format
        self.file_size = file_size

    def __str__(self):
        return (
        f"{super().__str__()}\n"
        f"파일 형식 : {self.file_format}\n"
        f"파일 크기 : {self.file_size}MB"
    )

class GeneralBook(Book):
    def __init__(self, isbn, title, author, location):
        super().__init__(isbn, title, author)
        self.location = location

    def __str__(self):
        return (
        f"{super().__str__()}\n"
        f"보관 위치 : {self.location}"
    )