"""Create User

Revision ID: 6fc038d73c3e
Revises: e939642a0d35
Create Date: 2025-05-28 00:51:19.225945

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from migrations.organisation import for_each_org_schema

# revision identifiers, used by Alembic.
revision: str = "6fc038d73c3e"
down_revision: Union[str, None] = "e939642a0d35"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


@for_each_org_schema
def upgrade(schema: str) -> None:
    """Upgrade schema."""
    preparer = sa.sql.compiler.IdentifierPreparer(op.get_bind().dialect)
    schema_quoted = preparer.format_schema(schema)

    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),  # email is unique, index=True
        sa.Column(
            "hashed_password", sa.String(), nullable=True
        ),  # Nullable if not always set immediately
        sa.Column("is_admin", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        schema=schema,
    )
    op.create_index(
        op.f("ix_id"), "users", ["id"], unique=False, schema=schema
    )
    op.create_index(
        op.f("ix_email"), "users", ["email"], unique=True, schema=schema
    )


@for_each_org_schema
def downgrade(schema: str) -> None:
    """Downgrade schema."""
    preparer = sa.sql.compiler.IdentifierPreparer(op.get_bind().dialect)
    schema_quoted = preparer.format_schema(schema)

    op.drop_index(op.f("ix_email"), table_name="users", schema=schema)
    op.drop_index(op.f("ix_id"), table_name="users", schema=schema)
    op.drop_table("users", schema=schema)
