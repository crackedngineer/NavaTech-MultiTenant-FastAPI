import functools
from typing import Callable

from typeguard import typechecked
import sqlalchemy as sa
from alembic import op


@typechecked
def for_each_org_schema(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped():
        schemas = op.get_bind().execute(sa.text("SELECT schema FROM shared.organisations")).fetchall()
        for (schema,) in schemas:
            func(schema)

    return wrapped
