"""empty message

Revision ID: 8146fefd1f4a
Revises: da83ec9f51d2
Create Date: 2023-08-21 16:53:08.910779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8146fefd1f4a'
down_revision = 'da83ec9f51d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fund_request', schema=None) as batch_op:
        batch_op.add_column(sa.Column('approval_level', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fund_request', schema=None) as batch_op:
        batch_op.drop_column('approval_level')

    # ### end Alembic commands ###
