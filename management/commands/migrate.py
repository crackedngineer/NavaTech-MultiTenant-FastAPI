import os
import typer
from app.database.engine import engine
from sqlalchemy.schema import CreateSchema
from alembic import command
from alembic.config import Config
from alembic.runtime.migration import MigrationContext
from app.models.base import get_shared_metadata, Base

app = typer.Typer()


@app.command(name="migrate")
def migrate():
    """Migrate DB"""
    typer.echo(" Migrate a new DB")
    _migrate()
    typer.echo(" Migration completed successfully")


def _migrate():
    with engine.begin() as db:
        alembic_config = Config("alembic.ini")
        context = MigrationContext.configure(db)
        if context.get_current_revision() is not None:
            print("Database already exists.")
            return

        db.execute(CreateSchema("shared"))
        get_shared_metadata().create_all(bind=db)

        alembic_config.attributes["connection"] = db
        command.stamp(alembic_config, "head", purge=True)
