"""empty message

Revision ID: e1585cfff8b5
Revises: 
Create Date: 2024-11-21 16:35:17.433429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1585cfff8b5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Administrador',
    sa.Column('IdAdm', sa.Integer(), nullable=False),
    sa.Column('Nome', sa.String(length=45), nullable=True),
    sa.Column('Email', sa.String(length=45), nullable=True),
    sa.Column('CPF', sa.String(length=15), nullable=True),
    sa.Column('Senha', sa.String(length=45), nullable=True),
    sa.PrimaryKeyConstraint('IdAdm')
    )
    op.create_table('Noticia',
    sa.Column('IdNoticia', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('Titulo', sa.String(length=45), nullable=True),
    sa.Column('Data_publicacao', sa.Date(), nullable=True),
    sa.Column('Texto', sa.Text(), nullable=True),
    sa.Column('IdAdm', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['IdAdm'], ['Administrador.IdAdm'], ),
    sa.PrimaryKeyConstraint('IdNoticia')
    )
    op.create_table('Projeto',
    sa.Column('IdProjeto', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('Titulo', sa.String(length=45), nullable=True),
    sa.Column('Data_inicio', sa.Date(), nullable=True),
    sa.Column('Data_fim', sa.Date(), nullable=True),
    sa.Column('pStatus', sa.String(length=45), nullable=True),
    sa.Column('Texto', sa.Text(), nullable=True),
    sa.Column('IdAdm', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['IdAdm'], ['Administrador.IdAdm'], ),
    sa.PrimaryKeyConstraint('IdProjeto')
    )
    op.create_table('Animal',
    sa.Column('IdAnimal', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('aStatus', sa.String(length=45), nullable=True),
    sa.Column('Nome', sa.String(length=45), nullable=True),
    sa.Column('Especie', sa.String(length=45), nullable=True),
    sa.Column('Porte', sa.String(length=45), nullable=True),
    sa.Column('IdProjeto', sa.Integer(), nullable=False),
    sa.Column('IdAdm', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['IdAdm'], ['Administrador.IdAdm'], ),
    sa.ForeignKeyConstraint(['IdProjeto'], ['Projeto.IdProjeto'], ),
    sa.PrimaryKeyConstraint('IdAnimal')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Animal')
    op.drop_table('Projeto')
    op.drop_table('Noticia')
    op.drop_table('Administrador')
    # ### end Alembic commands ###
