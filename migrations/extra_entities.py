"""Module defining entities that should be registered"""
from pathlib import Path

from alembic_utils.pg_function import PGFunction
from alembic_utils.replaceable_entity import register_entities

FUNCTIONS_DIR = Path(__file__).parent.absolute() / "resources"


def define_postgres_function(location: Path, file: str) -> PGFunction:
    """Helper to define a postgres function"""
    return PGFunction(
        schema="main",
        signature=(location / f"{file}.signature").read_text(),
        definition=(location / f"{file}.sql").read_text()
    )


def get_functions(functions_dir: Path):
    """Helper to get all functions listed in the path to be registered"""
    return [define_postgres_function(functions_dir, f.stem) for f in (functions_dir).iterdir() if f.suffix == ".sql"]


def register_all():
    """Entry point to register all functions"""
    objects_to_register = get_functions(functions_dir=FUNCTIONS_DIR)
    register_entities(entities=objects_to_register)
