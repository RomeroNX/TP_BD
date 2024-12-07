"""Add new field to table

Revision ID: 3f601e13ec23
Revises: 
Create Date: 2024-10-15 17:22:12.695915

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '3f601e13ec23'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Додаємо нове поле 'Address' до таблиці 'Customer'
    op.add_column('Customer', sa.Column('Address', sa.String(length=100), nullable=True))


def downgrade() -> None:
    # Видаляємо поле 'Address' при відкаті міграції
    op.drop_column('Customer', 'Address')
