"""empty message

Revision ID: cbe0dcc14e4f
Revises: 2105208df19c
Create Date: 2022-05-12 15:59:07.052607

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbe0dcc14e4f'
down_revision = '2105208df19c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.String(length=64), nullable=True))
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    op.drop_constraint('user_password_key', 'user', type_='unique')
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.create_unique_constraint('user_password_key', 'user', ['password'])
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    op.drop_column('user', 'username')
    # ### end Alembic commands ###
