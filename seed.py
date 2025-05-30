from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timezone
from app.Models.members import Member
from app.Models.books import Book
from app.Models.guest import Guest
from app.Models.borrowed_books import BorrowedBook
from app.Models.guest_reading import GuestReading
from app.Models.genre import Genre
from app.Models.books_genre import BookGenre

def seed_data():
    engine = create_engine("sqlite:///app/db/library.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Clear existing data (optional but useful during testing)
    session.query(BorrowedBook).delete()
    session.query(GuestReading).delete()
    session.query(BookGenre).delete()
    session.query(Member).delete()
    session.query(Book).delete()
    session.query(Guest).delete()
    session.query(Genre).delete()

    # Members
    member1 = Member(name="Yasir", email="YAsir@gmail.com", membership_no=101)
    member2 = Member(name="Moha", email="moha@example.com", membership_no=102)
    
    
    

    # Books
    book1 = Book(title="Python Basics", author="ABDI", available_copies=3)
    book2 = Book(title="Advanced SQL", author="Jane", available_copies=2)

    # Guests
    guest1 = Guest(name="ALI")
    guest2 = Guest(name="SMITH")

    # Genres
    genre1 = Genre(name="Programming")
    genre2 = Genre(name="Database")

    # Book-Genre Relationships
    book_genre1 = BookGenre(books_id=1, genre_id=1)
    book_genre2 = BookGenre(books_id=2, genre_id=2)

    # Borrowed Books
    borrowed1 = BorrowedBook(members_id=1, books_id=1, borrowed_date=datetime.now(timezone.utc))
    borrowed2 = BorrowedBook(members_id=2, books_id=2, borrowed_date=datetime.now(timezone.utc))
    
    # Guest Reading
    reading1 = GuestReading(books_field=1, guest_id=1, time=datetime.now(timezone.utc))
    reading2 = GuestReading(books_field=2, guest_id=2, time=datetime.now(timezone.utc))

    # Add all to session
    session.add_all([
        member1, member2, book1, book2, guest1, guest2,
        genre1, genre2, book_genre1, book_genre2,
        borrowed1, borrowed2, reading1, reading2
    ])

    session.commit()
    session.close()
    print("📦 Seeded data into the database.")

if __name__ == "__main__":
    seed_data()