"""recipient email

Revision ID: bf9bec6a2cc4
Revises: 532a5f5e3366
Create Date: 2023-07-22 20:06:35.896221

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf9bec6a2cc4'
down_revision = '532a5f5e3366'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('email_recipient',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('email_recipient')
    # ### end Alembic commands ###
