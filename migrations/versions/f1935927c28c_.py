"""empty message

Revision ID: f1935927c28c
Revises: 
Create Date: 2020-06-25 23:36:09.851581

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1935927c28c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('business',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('business_name', sa.String(length=80), nullable=False),
    sa.Column('address', sa.String(length=120), nullable=False),
    sa.Column('phone_number', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('password')
    )
    op.create_table('visitor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('last_name', sa.String(length=120), nullable=False),
    sa.Column('age', sa.String(length=80), nullable=False),
    sa.Column('address', sa.String(length=120), nullable=False),
    sa.Column('phone_number', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('visit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(length=120), nullable=False),
    sa.Column('business_id', sa.Integer(), nullable=True),
    sa.Column('visitor_id', sa.Integer(), nullable=False),
    sa.Column('entry', sa.DateTime(timezone=120), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('result', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['business_id'], ['business.id'], ),
    sa.ForeignKeyConstraint(['visitor_id'], ['visitor.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('image')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('visit')
    op.drop_table('visitor')
    op.drop_table('business')
    # ### end Alembic commands ###
