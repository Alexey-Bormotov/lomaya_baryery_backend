"""init

Revision ID: d37fa6413c00
Revises: 
Create Date: 2022-09-20 12:33:13.501170

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd37fa6413c00'
down_revision = None
branch_labels = None
depends_on = None


REQUEST_STATUS_TYPE = sa.Enum('approved', 'declined', 'pending', 'repeated request', name='request_status')
REQUEST_STATUS_TYPE_PG = postgresql.ENUM('approved', 'declined', 'pending', 'repeated request', name='request_status')

SHIFT_STATUS_TYPE = sa.Enum('started', 'finished', 'preparing', 'cancelled', name='shift_status')
SHIFT_STATUS_TYPE_PG = postgresql.ENUM('started', 'finished', 'preparing', 'cancelled', name='shift_status')

USER_TASK_STATUS_TYPE = sa.Enum('new', 'under_review', 'approved', 'declined', name='user_task_status')
USER_TASK_STATUS_TYPE_PG = postgresql.ENUM('new', 'under_review', 'approved', 'declined', name='user_task_status')

REQUEST_STATUS_TYPE.with_variant(REQUEST_STATUS_TYPE_PG, 'postgresql')
SHIFT_STATUS_TYPE.with_variant(SHIFT_STATUS_TYPE_PG, 'postgresql')
USER_TASK_STATUS_TYPE.with_variant(USER_TASK_STATUS_TYPE_PG, 'postgresql')


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('photos',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('url', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('url')
    )
    op.create_table('shifts',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('status', SHIFT_STATUS_TYPE, nullable=False),
    sa.Column('started_at', sa.DATE(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('finished_at', sa.DATE(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tasks',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('url', sa.String(length=150), nullable=False),
    sa.Column('description', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('description'),
    sa.UniqueConstraint('url')
    )
    op.create_table('users',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('surname', sa.String(length=100), nullable=False),
    sa.Column('date_of_birth', sa.DATE(), nullable=False),
    sa.Column('city', sa.String(length=50), nullable=False),
    sa.Column('phone_number', sa.String(length=11), nullable=False),
    sa.Column('telegram_id', sa.BigInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone_number'),
    sa.UniqueConstraint('telegram_id')
    )
    op.create_table('requests',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('shift_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('status', REQUEST_STATUS_TYPE, nullable=False),
    sa.ForeignKeyConstraint(['shift_id'], ['shifts.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_tasks',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('shift_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('task_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('day_number', sa.Integer(), nullable=True),
    sa.Column('status', USER_TASK_STATUS_TYPE, nullable=False),
    sa.Column('photo_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['photo_id'], ['photos.id'], ),
    sa.ForeignKeyConstraint(['shift_id'], ['shifts.id'], ),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id', 'shift_id', 'task_id', name='_user_task_uc')
    )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_tasks')
    op.drop_table('requests')
    op.drop_table('users')
    op.drop_table('tasks')
    op.drop_table('shifts')
    op.drop_table('photos')
    ### drop types
    SHIFT_STATUS_TYPE.drop(op.get_bind(), checkfirst=True)
    REQUEST_STATUS_TYPE.drop(op.get_bind(), checkfirst=True)
    USER_TASK_STATUS_TYPE.drop(op.get_bind(), checkfirst=True)
    # ### end Alembic commands ###
