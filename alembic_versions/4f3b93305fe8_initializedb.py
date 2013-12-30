"""initializedb

Revision ID: 4f3b93305fe8
Revises: None
Create Date: 2013-12-15 16:12:06.500297

"""

# revision identifiers, used by Alembic.
revision = '4f3b93305fe8'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.Unicode(length=255), nullable=True),
    sa.Column('name', sa.Unicode(length=255), nullable=True),
    sa.Column('password', sa.Unicode(length=60), nullable=True),
    sa.Column('email', sa.Unicode(length=255), nullable=True),
    sa.Column('activated', sa.Boolean(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.Column('signup', sa.DateTime(), nullable=True),
    sa.Column('api_key', sa.Unicode(length=12), nullable=True),
    sa.Column('invite_ct', sa.Integer(), nullable=True),
    sa.Column('invited_by', sa.Unicode(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('logging',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user', sa.Unicode(length=255), nullable=False),
    sa.Column('component', sa.Unicode(length=50), nullable=False),
    sa.Column('status', sa.Unicode(length=10), nullable=False),
    sa.Column('message', sa.Unicode(length=255), nullable=False),
    sa.Column('payload', sa.UnicodeText(), nullable=True),
    sa.Column('tstamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table(u'activations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.Unicode(length=60), nullable=True),
    sa.Column('valid_until', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.Unicode(length=255), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table(u'activations')
    op.drop_table('logging')
    op.drop_table('users')
    ### end Alembic commands ###
