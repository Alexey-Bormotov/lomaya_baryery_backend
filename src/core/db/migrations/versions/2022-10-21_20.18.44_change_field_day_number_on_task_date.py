"""change_field_day_number_on_task_date

Revision ID: 415099a58080
Revises: a3e955efe582
Create Date: 2022-10-21 20:18:44.858465

"""
from datetime import date

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '415099a58080'
down_revision = 'a3e955efe582'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_tasks', sa.Column('task_date', sa.DATE(), nullable=False))
    op.drop_column('user_tasks', 'day_number')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_tasks', sa.Column('day_number', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('user_tasks', 'task_date')
    # ### end Alembic commands ###
