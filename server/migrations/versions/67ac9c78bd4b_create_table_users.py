"""Create table users

Revision ID: 67ac9c78bd4b
Revises: 
Create Date: 2024-02-10 08:43:21.918780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67ac9c78bd4b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('_password_hash', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
