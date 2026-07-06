"""add content column to posts table

Revision ID: 3e93d12c9c4a
Revises: 7debb99191ac
Create Date: 2026-07-06 12:54:23.201742

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e93d12c9c4a'
down_revision = '7debb99191ac'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
