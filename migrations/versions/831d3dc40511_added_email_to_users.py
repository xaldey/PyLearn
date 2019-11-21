"""added email to users

Revision ID: 831d3dc40511
Revises: 0c1c9d117547
Create Date: 2019-11-21 11:43:18.724827

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '831d3dc40511'
down_revision = '0c1c9d117547'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'email')
    # ### end Alembic commands ###
