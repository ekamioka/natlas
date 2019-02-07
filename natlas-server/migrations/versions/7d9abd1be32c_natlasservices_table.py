"""NatlasServices table

Revision ID: 7d9abd1be32c
Revises: 3fb710fe0fe1
Create Date: 2019-02-07 03:00:36.999599

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d9abd1be32c'
down_revision = '3fb710fe0fe1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('natlas_services',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sha256', sa.String(length=64), nullable=True),
    sa.Column('services', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('natlas_services')
    # ### end Alembic commands ###
