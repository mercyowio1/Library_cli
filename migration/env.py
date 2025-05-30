from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# this is the Alembic Config object, which provides access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# === IMPORT BASE AND ALL MODELS ===
from app.Models.base import Base
from app.Models.members import Member
from app.Models.books import Book
from app.Models.guest import Guest
from app.Models.borrowed_books import BorrowedBook
from app.Models.genre import Genre
from app.Models.books_genre import BookGenre
from app.Models.guest_reading import GuestReading

# Set Alembic target metadata to Base.metadata (for autogenerate)
target_metadata = Base.metadata

# Run migrations in 'offline' mode.
def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

# Run migrations in 'online' mode.
def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

# Entry point: run offline or online migration mode.
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()