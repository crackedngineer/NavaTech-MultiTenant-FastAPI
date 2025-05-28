"""Create Org Default schema

Revision ID: 2b118ad5a632
Revises: f4c61247c25b
Create Date: 2025-05-26 11:16:05.943233

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '2b118ad5a632'
down_revision: Union[str, None] = 'f4c61247c25b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("CREATE SCHEMA IF NOT EXISTS org_default")


def downgrade() -> None:
    """Downgrade schema."""
    pass