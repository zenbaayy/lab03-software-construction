"""Lab 03 - Lab Task 2: Class/design model for a library borrowing system.

UML-style sketch:

    Member 1 ---- * Loan * ---- 1 Book
         \\                      /
          \\                    /
           ------ Library ------
        (Library owns books, members and loans)
"""

from dataclasses import dataclass, field
from datetime import date, timedelta

MAX_LOANS_PER_MEMBER = 3
LOAN_DAYS = 14


@dataclass
class Book:
    isbn: str
    title: str
    available: bool = True


@dataclass
class Member:
    member_id: int
    name: str


@dataclass
class Loan:
    book: Book
    member: Member
    due_date: date
    returned: bool = False


@dataclass
class Library:
    books: dict = field(default_factory=dict)
    members: dict = field(default_factory=dict)
    loans: list = field(default_factory=list)

    def add_book(self, book):
        self.books[book.isbn] = book

    def add_member(self, member):
        self.members[member.member_id] = member

    def active_loans(self, member_id):
        return [
            loan
            for loan in self.loans
            if loan.member.member_id == member_id and not loan.returned
        ]

    def borrow(self, isbn, member_id, today=None):
        today = today or date.today()
        book = self.books[isbn]
        member = self.members[member_id]
        if not book.available:
            raise ValueError("Book is already borrowed")
        if len(self.active_loans(member_id)) >= MAX_LOANS_PER_MEMBER:
            raise ValueError("Member reached the loan limit")
        book.available = False
        loan = Loan(book, member, today + timedelta(days=LOAN_DAYS))
        self.loans.append(loan)
        return loan

    def return_book(self, isbn, member_id):
        for loan in self.active_loans(member_id):
            if loan.book.isbn == isbn:
                loan.returned = True
                loan.book.available = True
                return loan
        raise ValueError("No active loan found for this book and member")


if __name__ == "__main__":
    lib = Library()
    lib.add_book(Book("111", "Clean Code"))
    lib.add_book(Book("222", "Code Complete"))
    lib.add_member(Member(1, "Aqsa"))

    loan = lib.borrow("111", 1)
    print("Borrowed:", loan.book.title, "| due:", loan.due_date)
    try:
        lib.borrow("111", 1)
    except ValueError as err:
        print("Error:", err)
    lib.return_book("111", 1)
    print("Returned. Available again:", lib.books["111"].available)
