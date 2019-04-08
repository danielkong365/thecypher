"""Add Start Time and End Time

Revision ID: 473e3d1ea965
Revises: 46fa5502734e
Create Date: 2019-02-07 12:14:00.234341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '473e3d1ea965'
down_revision = '46fa5502734e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('end_time', sa.Time(), nullable=True))
    op.add_column('event', sa.Column('start_time', sa.Time(), nullable=True))
    op.create_index(op.f('ix_event_end_time'), 'event', ['end_time'], unique=False)
    op.create_index(op.f('ix_event_start_time'), 'event', ['start_time'], unique=False)
    op.add_column('session', sa.Column('end_time', sa.Time(), nullable=True))
    op.add_column('session', sa.Column('start_time', sa.Time(), nullable=True))
    op.create_index(op.f('ix_session_end_time'), 'session', ['end_time'], unique=False)
    op.create_index(op.f('ix_session_start_time'), 'session', ['start_time'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_session_start_time'), table_name='session')
    op.drop_index(op.f('ix_session_end_time'), table_name='session')
    op.drop_column('session', 'start_time')
    op.drop_column('session', 'end_time')
    op.drop_index(op.f('ix_event_start_time'), table_name='event')
    op.drop_index(op.f('ix_event_end_time'), table_name='event')
    op.drop_column('event', 'start_time')
    op.drop_column('event', 'end_time')
    # ### end Alembic commands ###