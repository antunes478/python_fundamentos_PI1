"""create_product_table

Revision ID: 51000d54d3a8
Revises: 568ca154f635
Create Date: 2024-06-03 21:08:34.189354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51000d54d3a8'
down_revision = '568ca154f635'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('category', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    # ### end Alembic commands ###
