"""empty message

Revision ID: e2c34162ac8b
Revises: 595bdc0fba63
Create Date: 2018-11-25 17:33:44.831189

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2c34162ac8b'
down_revision = '595bdc0fba63'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('location', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_user_location'), 'user', ['location'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_location'), table_name='user')
    op.drop_column('user', 'location')
    # ### end Alembic commands ###