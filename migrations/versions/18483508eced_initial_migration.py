"""Initial Migration

Revision ID: 18483508eced
Revises: e31a3025b87e
Create Date: 2021-02-25 15:47:25.833930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18483508eced'
down_revision = 'e31a3025b87e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_secure')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_secure', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
