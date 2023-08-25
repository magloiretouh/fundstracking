"""empty message

Revision ID: 164feb28ecc9
Revises: f9346f1391b8
Create Date: 2023-08-24 10:43:24.685189

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '164feb28ecc9'
down_revision = 'f9346f1391b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fund_request', schema=None) as batch_op:
        batch_op.alter_column('odm_filename',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fund_request', schema=None) as batch_op:
        batch_op.alter_column('odm_filename',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)

    # ### end Alembic commands ###
