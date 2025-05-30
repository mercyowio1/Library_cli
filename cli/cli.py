import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.Models.base import Base
from app.Models.members import Member
from app.Models.books import Book
from app.Models.guest import Guest

# Database setup
def get_engine():
    return create_engine("sqlite:///app/db/library.db")

def get_session():
    Session = sessionmaker(bind=get_engine())
    return Session()

def create_tables():
    Base.metadata.create_all(get_engine())
    print(" Tables created (if not already existing)")

# Members Menu
def members_menu():
    session = get_session()

    while True:
        click.echo("\nMembers Menu:")
        click.echo(" a. Add member")
        click.echo(" b. Remove member")
        click.echo(" c. List members")
        click.echo(" d. Back to main menu")

        choice = input("Choose an option: ").strip().lower()

        if choice == 'a':
            name = input("Enter member name: ")
            email = input("Enter member email: ")
            membership_no = input("Enter membership number: ")
            new_member = Member(name=name, email=email, membership_no=membership_no)
            session.add(new_member)
            session.commit()
            click.echo(f" Added member: {name}, Email: {email}, Membership No: {membership_no}")

        elif choice == 'b':
            member_id = input("Enter member ID to remove: ")
            member = session.query(Member).filter_by(id=member_id).first()
            if member:
                session.delete(member)
                session.commit()
                click.echo(f" Removed member with ID {member_id}")
            else:
                click.echo(" Member not found.")

        elif choice == 'c':
            members = session.query(Member).all()
            click.echo(" All Members:")
            for m in members:
                click.echo(f" - ID: {m.id}, Name: {m.name}, Email: {m.email}, No: {m.membership_no}")

        elif choice == 'd':
            session.close()
            break
        else:
            click.echo(" Invalid choice. Try again.")

# Books Menu
def books_menu():
    session = get_session()

    while True:
        click.echo("\nBooks Menu:")
        click.echo(" a. Add book")
        click.echo(" b. Remove book")
        click.echo(" c. List books")
        click.echo(" d. Back to main menu")

        choice = input("Choose an option: ").strip().lower()

        if choice == 'a':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            available_copies = int(input("Enter available copies: ")) 
            new_book = Book(title=title, author=author, available_copies=available_copies)
            session.add(new_book)
            session.commit()
            click.echo(f" Added book: {title} by {author}")

        elif choice == 'b':
            book_id = input("Enter book ID to remove: ")
            book = session.query(Book).filter_by(id=book_id).first()
            if book:
                session.delete(book)
                session.commit()
                click.echo(f" Removed book with ID {book_id}")
            else:
                click.echo(" Book not found.")

        elif choice == 'c':
            books = session.query(Book).all()
            click.echo(" All Books:")
            for b in books:
                click.echo(f" - ID: {b.id}, Title: {b.title}, Author: {b.author}, Available Copies: {b.available_copies}")

        elif choice == 'd':
            session.close()
            break
        else:
            click.echo(" Invalid choice. Try again.")


# Guests Menu
def guests_menu():
    session = get_session()

    while True:
        click.echo("\nGuests Menu:")
        click.echo(" a. Add guest")
        click.echo(" b. Remove guest")
        click.echo(" c. List guests")
        click.echo(" d. Back to main menu")

        choice = input("Choose an option: ").strip().lower()

        if choice == 'a':
            name = input("Enter guest name: ")
            new_guest = Guest(name=name)
            session.add(new_guest)
            session.commit()
            click.echo(f" Added guest: {name}")

        elif choice == 'b':
            guest_id = input("Enter guest ID to remove: ")
            guest = session.query(Guest).filter_by(id=guest_id).first()
            if guest:
                session.delete(guest)
                session.commit()
                click.echo(f" Removed guest with ID {guest_id}")
            else:
                click.echo(" Guest not found.")

        elif choice == 'c':
            guests = session.query(Guest).all()
            click.echo("🎟️ All Guests:")
            for g in guests:
                click.echo(f" - ID: {g.id}, Name: {g.name}")

        elif choice == 'd':
            session.close()
            break
        else:
            click.echo("Invalid choice. Try again.")

# Main Menu
@click.command()
def main_menu():
    create_tables()

    while True:
        click.echo("\n Library System Main Menu:")
        click.echo("1. Members")
        click.echo("2. Books")
        click.echo("3. Guests")
        click.echo("4. Exit")

        choice = input("Select an option: ").strip()

        if choice == '1':
            members_menu()
        elif choice == '2':
            books_menu()
        elif choice == '3':
            guests_menu()
        elif choice == '4':
            click.echo("Goodbye!")
            break
        else:
            click.echo(" Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main_menu()