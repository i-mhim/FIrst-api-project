"""create posts table

Revision ID: 7debb99191ac
Revises: 
Create Date: 2026-07-06 12:43:21.352640

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7debb99191ac'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))


def downgrade():
    op.drop_table('posts')
    pass
