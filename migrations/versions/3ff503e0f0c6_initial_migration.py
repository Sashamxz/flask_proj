"""Initial migration.

Revision ID: 3ff503e0f0c6
Revises: 
Create Date: 2021-08-04 11:13:44.653583

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ff503e0f0c6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('slug', sa.String(length=140), nullable=True))
    op.drop_constraint('post_slag_key', 'post', type_='unique')
    op.create_unique_constraint(None, 'post', ['slug'])
    op.drop_column('post', 'slag')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('slag', sa.VARCHAR(length=140), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'post', type_='unique')
    op.create_unique_constraint('post_slag_key', 'post', ['slag'])
    op.drop_column('post', 'slug')
    # ### end Alembic commands ###
