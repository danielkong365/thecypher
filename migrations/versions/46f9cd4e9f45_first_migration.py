"""First migration

Revision ID: 46f9cd4e9f45
Revises: 
Create Date: 2019-01-22 12:02:41.355999

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46f9cd4e9f45'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('location', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_location'), 'user', ['location'], unique=False)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(length=64), nullable=True),
    sa.Column('address', sa.String(length=128), nullable=True),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('description', sa.String(length=1024), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('datetime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_event_address'), 'event', ['address'], unique=False)
    op.create_index(op.f('ix_event_description'), 'event', ['description'], unique=False)
    op.create_index(op.f('ix_event_location'), 'event', ['location'], unique=False)
    op.create_index(op.f('ix_event_title'), 'event', ['title'], unique=False)
    op.create_table('session',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(length=64), nullable=True),
    sa.Column('address', sa.String(length=128), nullable=True),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('description', sa.String(length=1024), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('datetime', sa.DateTime(), nullable=True),
    sa.Column('reoccuring', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_session_address'), 'session', ['address'], unique=False)
    op.create_index(op.f('ix_session_description'), 'session', ['description'], unique=False)
    op.create_index(op.f('ix_session_location'), 'session', ['location'], unique=False)
    op.create_index(op.f('ix_session_title'), 'session', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_session_title'), table_name='session')
    op.drop_index(op.f('ix_session_location'), table_name='session')
    op.drop_index(op.f('ix_session_description'), table_name='session')
    op.drop_index(op.f('ix_session_address'), table_name='session')
    op.drop_table('session')
    op.drop_index(op.f('ix_event_title'), table_name='event')
    op.drop_index(op.f('ix_event_location'), table_name='event')
    op.drop_index(op.f('ix_event_description'), table_name='event')
    op.drop_index(op.f('ix_event_address'), table_name='event')
    op.drop_table('event')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_location'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
