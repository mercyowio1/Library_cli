from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.Models.members import Member
from app.Models.books import Book
from app.Models.guest import Guest
from app.Models.borrowed_books import BorrowedBook
from app.Models.guest_reading import GuestReading
from app.Models.genre import Genre
from app.Models.books_genre import BookGenre

def debug_db():
    try:
        engine = create_engine("sqlite:///app/db/library.db")
        Session = sessionmaker(bind=engine)
        session = Session()

        print("\n=== MEMBERS ===")
        for member in session.query(Member).all():
            print(f"ID: {member.id}, Name: {member.name}, Email: {member.email}, Membership No: {member.membership_no}")

        print("\n=== BOOKS ===")
        for book in session.query(Book).all():
            print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Available: {book.available_copies}")

        print("\n=== GUESTS ===")
        for guest in session.query(Guest).all():
            print(f"ID: {guest.id}, Name: {guest.name}")

        print("\n=== BORROWED BOOKS ===")
        for bb in session.query(BorrowedBook).all():
            print(f"ID: {bb.id}, Member ID: {bb.members_id}, Book ID: {bb.books_id}, Borrowed: {bb.borrowed_date}, Returned: {bb.return_date}")
        

        print("\n=== GUEST READINGS ===")
        for gr in session.query(GuestReading).all():
            print(f"ID: {gr.id}, Guest ID: {gr.guest_id}, Book ID: {gr.book.id}, Time: {gr.time}")

        print("\n=== GENRES ===")
        for genre in session.query(Genre).all():
            print(f"ID: {genre.id}, Name: {genre.name}")

        print("\n=== BOOK-GENRE RELATIONSHIPS ===")
        for bg in session.query(BookGenre).all():
            print(f"Book ID: {bg.books_id}, Genre ID: {bg.genre_id}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    debug_db()