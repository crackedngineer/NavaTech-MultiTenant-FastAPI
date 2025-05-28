"""Create organisations table

Revision ID: e939642a0d35
Revises: 2b118ad5a632
Create Date: 2025-05-27 00:46:15.187839

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e939642a0d35"
down_revision: Union[str, None] = "2b118ad5a632"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE SCHEMA IF NOT EXISTS shared")

    op.create_table(
        "organisations",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("schema", sa.String(256), nullable=False),
        sa.Column("host", sa.String(256), nullable=False),
        sa.Column("email", sa.String(256), nullable=False),
        sa.Column(
            "status",
            sa.Enum(
                "active",
                "inactive",
                name="status",
                schema="shared",
                inherit_schema=True,
            ),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_organisations")),
        sa.UniqueConstraint("schema", name=op.f("uq_organisations_schema")),
        sa.UniqueConstraint("host", name=op.f("uq_organisations_host")),
        schema="shared",
    )
    op.create_index(
        op.f("ix_name"),
        "organisations",
        ["name"],
        unique=False,
        schema="shared",
    )


def downgrade() -> None:
    op.drop_index(
        op.f("ix_name"), table_name="organisations", schema="shared"
    )
    op.drop_table("organisations", schema="shared")
    op.execute("DROP TYPE IF EXISTS shared.status")
