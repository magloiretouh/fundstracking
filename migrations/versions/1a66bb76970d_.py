"""empty message

Revision ID: 1a66bb76970d
Revises: 8843e3699543
Create Date: 2023-08-21 11:32:08.750708

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a66bb76970d'
down_revision = '8843e3699543'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('grade_zone', schema=None) as batch_op:
        batch_op.alter_column('montant_peage',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('grade_zone', schema=None) as batch_op:
        batch_op.alter_column('montant_peage',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
