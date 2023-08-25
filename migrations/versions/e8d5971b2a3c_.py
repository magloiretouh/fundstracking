"""empty message

Revision ID: e8d5971b2a3c
Revises: 2c46d697c84f
Create Date: 2023-08-21 11:03:33.955784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8d5971b2a3c'
down_revision = '2c46d697c84f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('grade', schema=None) as batch_op:
        batch_op.drop_column('montant_perdiem')
        batch_op.drop_column('montant_logement')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('grade', schema=None) as batch_op:
        batch_op.add_column(sa.Column('montant_logement', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('montant_perdiem', sa.INTEGER(), autoincrement=False, nullable=False))

    # ### end Alembic commands ###