"""empty message

Revision ID: 14ca8d76aed6
Revises: 179f674d84c1
Create Date: 2023-09-27 10:06:46.437031

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14ca8d76aed6'
down_revision = '179f674d84c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fund_request', schema=None) as batch_op:
        batch_op.add_column(sa.Column('superieur_hierarchique_username', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('dga_username', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fund_request', schema=None) as batch_op:
        batch_op.drop_column('dga_username')
        batch_op.drop_column('superieur_hierarchique_username')

    # ### end Alembic commands ###