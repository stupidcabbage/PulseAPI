"""like table

Revision ID: b03ea2f58e44
Revises: 74ddfb15f4d1
Create Date: 2024-03-03 18:05:34.622851

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = 'b03ea2f58e44'
down_revision: Union[str, None] = '74ddfb15f4d1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'users', 'countries', ['country_code'], ['alpha2'], use_alter=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    # ### end Alembic commands ###
