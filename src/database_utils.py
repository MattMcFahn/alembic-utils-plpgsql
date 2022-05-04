"""Helper utilities for a postgres DB"""

from functools import lru_cache

from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine


def postgres_url(user: str, password: str, host: str, port: str, database_name: str) -> str:
    """Return a postgres url"""
    return f"postgresql://{user}:{password}@{host}:{port}/{database_name}"


@lru_cache
def db_engine() -> Engine:
    """SQLAlchemy core database engine"""
    db_url = postgres_url(
        getenv("SINK_USER", "user"),
        getenv("PASSWORD", "secret"),
        getenv("SINK_HOST", "localhost"),
        getenv("SINK_PORT", "5432"),
        getenv("SINK_NAME", "test_db"),
    )
    return create_engine(db_url)


