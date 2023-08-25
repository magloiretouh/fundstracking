"""empty message

Revision ID: 197d972167ad
Revises: 
Create Date: 2023-08-18 12:49:40.312739

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '197d972167ad'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('activity_domain',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('libelle', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cost_center',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('libelle', sa.String(length=255), nullable=False),
    sa.Column('code', sa.String(length=12), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employee_request',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fund_request', sa.String(length=25), nullable=False),
    sa.Column('employe', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('grade',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('libelle', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('zone',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('libelle', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom_prenoms', sa.String(length=255), nullable=False),
    sa.Column('code', sa.String(length=25), nullable=False),
    sa.Column('fonction', sa.String(length=255), nullable=False),
    sa.Column('grade', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['grade'], ['grade.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fund_request',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('request_track_id', sa.String(length=25), nullable=False),
    sa.Column('itineraire', sa.String(length=255), nullable=False),
    sa.Column('moyen_de_transport', sa.String(length=25), nullable=False),
    sa.Column('zone', sa.Integer(), nullable=False),
    sa.Column('but_de_la_mission', sa.String(length=255), nullable=False),
    sa.Column('date_debut', sa.DateTime(), nullable=False),
    sa.Column('date_fin', sa.DateTime(), nullable=False),
    sa.Column('domaine_activite', sa.Integer(), nullable=False),
    sa.Column('centre_de_cout', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['centre_de_cout'], ['cost_center.id'], ),
    sa.ForeignKeyConstraint(['domaine_activite'], ['activity_domain.id'], ),
    sa.ForeignKeyConstraint(['zone'], ['zone.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fund_request')
    op.drop_table('employee')
    op.drop_table('zone')
    op.drop_table('grade')
    op.drop_table('employee_request')
    op.drop_table('cost_center')
    op.drop_table('activity_domain')
    # ### end Alembic commands ###
