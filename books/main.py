from models import Book, EBook, GeneralBook, AlreadyBorrowedError, BookNotFoundError
from library import Library

library = Library()

book1 = GeneralBook(
    "9788970638331",
    "지금 알고 있는 걸 그때도 알았더라면",
    "류시화",
    "가 1-2"
)

book2 = GeneralBook(
    "9791187297901",
    "법륜 스님의 금강경 강의 필사 공책",
    "법륜",
    "나 1-3"
)

book3 = EBook(
    "9791173974373",
    "재물을 부르는 관상",
    "박광열",
    "EPUB",
    2.5
)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

while True:
    print("1. 책 등록")
    print("2. 전체 책 보기")
    print("3. 책 검색")
    print("4. 저자 목록")
    print("5. 책 대출")
    print("6. 책 반납")
    print("7. 책 삭제")
    print("0. 종료")

    choice = input("이용할 메뉴를 선택하세요 : ")

    if choice == "0":
        print("프로그램을 종료합니다.")
        break

    elif choice == "1":
        print("1. 일반 도서")
        print("2. 전자책")

        book_type = input("책 종류를 선택하세요 :")

        if book_type == "1":
            isbn = input("ISBN을 입력하세요 : ")
            title = input("제목을 입력하세요 : ")
            author = input("저자를 입력하세요 : ")
            location = input("보관 위치를 입력하세요 : ")

            book = GeneralBook(isbn, title, author, location)
            library.add_book(book)

        elif book_type == "2":
            isbn = input("ISBN을 입력하세요 : ")
            title = input("제목을 입력하세요 : ")
            author = input("저자를 입력하세요 : ")
            file_format = input("파일 형식을 입력하세요 : ")
            file_size = input("파일 크기(MB)를 입력하세요 : ")

            book = EBook(isbn, title, author, file_format, file_size)
            library.add_book(book)

    elif choice == "2":
        library.show_all_books()

    elif choice == "3":
        keyword = input("검색할 제목 또는 저자를 입력하세요 : ")
        library.search_available_books(keyword)

    elif choice == "4":
        library.show_authors()

    elif choice == "5":
        try:
            isbn = input("대출할 책의 ISBN을 입력하세요 : ")
            library.borrow_book(isbn)
        except AlreadyBorrowedError:
            print("이미 대출 중인 책입니다.")
        except BookNotFoundError:
            print("해당 ISBN의 책을 찾을 수 없습니다.")

    elif choice == "6":
        try:
            isbn = input("반납할 책의 ISBN을 입력하세요 : ")
            library.return_book(isbn)
        except BookNotFoundError:
            print("해당 ISBN의 책을 찾을 수 없습니다.")

    elif choice == "7":
        try:
            isbn = input("삭제할 책의 ISBN을 입력하세요 : ")
            library.delete_book(isbn)
        except BookNotFoundError:
            print("해당 ISBN의 책을 찾을 수 없습니다.")
