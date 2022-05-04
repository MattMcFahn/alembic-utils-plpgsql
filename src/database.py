"""Module for defining an ORM and interactions with the database"""

from sqlalchemy import Column, Integer, String, Table, MetaData
from src.database_utils import db_engine


main_schema = MetaData(bind=db_engine(), schema="main")
archive_schema = MetaData(bind=db_engine(), schema="archive")


test_table = Table(
    "test_table",
    main_schema,
    Column("id", String, primary_key=True),
    Column("some_column", Integer, nullable=True)
)

other_table = Table(
    "test_table_arch",
    archive_schema,
    Column("id", String, primary_key=False, nullable=False),
    Column("some_column", Integer, nullable=True)
)
