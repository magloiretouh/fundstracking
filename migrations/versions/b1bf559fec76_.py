"""empty message

Revision ID: b1bf559fec76
Revises: 197d972167ad
Create Date: 2023-08-18 15:08:27.050447

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1bf559fec76'
down_revision = '197d972167ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employee_request', schema=None) as batch_op:
        batch_op.add_column(sa.Column('fund_request', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('employee', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'employee', ['employee'], ['id'])
        batch_op.create_foreign_key(None, 'fund_request', ['fund_request'], ['id'])
        batch_op.drop_column('employe')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employee_request', schema=None) as batch_op:
        batch_op.add_column(sa.Column('employe', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('employee')
        batch_op.drop_column('fund_request')

    # ### end Alembic commands ###
