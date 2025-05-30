# Library system
A command-line interface (CLI) tool for managing a library system, built with Python. This application allows users to perform various library operations directly from the terminal.

# Features
1. Manage Books: Add, update, delete, and list books in the library.

2. Manage borrowed books: Check out and check in books for patrons.

3. Database Integration: Utilizes SQLAlchemy for database operations.

4. Migrations: Database schema migrations handled by Alembic.

5. Seeding: Populate the database with initial data using seed.py.

# Usage
After running the application, you can interact with the CLI to perform various operations. The available commands and their descriptions are as follows:

# Books
1. Add_book <title> <author>: Add a new book to the library.

2. Delete_book <book_id>: Remove a book from the library.

3. list_books: Display all books in the library.

# Borrowed_books
1. check_out <book_id> <member_id>: a member can borrow a book

2. check_in <book_id> <patron_id>: returning in a borrowed book

# members
1. add_member <name> <email>: Register a new member.


2. delete_member <member_id>: Remove a member from the system.

3. list_member: Display all member.

# Database
The application uses SQLAlchemy for ORM-based database interactions. The database schema is defined in app/models.py. Alembic is used for handling database migrations.
# To apply migrations:
`` alembic upgrade head ``
# To generate a new migration:
``alembic revision --autogenerate -m "Migration message" ``

# Seeding the Database
To populate the database with initial data, run:
``python seed.py``
This will insert predefined records into the database.

# Developer
Mercy Owino
# Github link 
[text](https://github.com/mercyowio1/Library_cli)