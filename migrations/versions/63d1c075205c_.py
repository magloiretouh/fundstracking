"""empty message

Revision ID: 63d1c075205c
Revises: 37e72556a491
Create Date: 2023-08-21 10:36:22.701224

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63d1c075205c'
down_revision = '37e72556a491'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('grade', schema=None) as batch_op:
        batch_op.alter_column('montant_perdiem',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('montant_logement',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('grade', schema=None) as batch_op:
        batch_op.alter_column('montant_logement',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('montant_perdiem',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###