"""re-start

Revision ID: 3f54a39b1b50
Revises: 
Create Date: 2023-04-02 22:25:34.515137

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f54a39b1b50'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    op.create_table('account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('type', sa.String(length=32), nullable=True),
    sa.Column('currency', sa.String(length=16), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('last_modified', sa.DateTime(), nullable=True),
    sa.Column('start_balance', sa.Float(precision=64), nullable=True),
    sa.Column('balance_date', sa.Date(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('balance_archive', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('account', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_account_balance_date'), ['balance_date'], unique=False)
        batch_op.create_index(batch_op.f('ix_account_created_at'), ['created_at'], unique=False)
        batch_op.create_index(batch_op.f('ix_account_last_modified'), ['last_modified'], unique=False)

    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('type', sa.String(length=32), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('competence', sa.String(length=32), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('last_modified', sa.DateTime(), nullable=True),
    sa.Column('budget', sa.Float(precision=64), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('icon', sa.String(length=255), nullable=True),
    sa.Column('budget_archive', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('category', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_category_created_at'), ['created_at'], unique=False)
        batch_op.create_index(batch_op.f('ix_category_last_modified'), ['last_modified'], unique=False)

    op.create_table('transaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account', sa.Integer(), nullable=True),
    sa.Column('category', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Float(precision=64), nullable=True),
    sa.Column('currency', sa.String(length=16), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('tag', sa.String(length=32), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['account'], ['account.id'], ),
    sa.ForeignKeyConstraint(['category'], ['category.id'], ),
    sa.ForeignKeyConstraint(['currency'], ['account.currency'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('transaction', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_transaction_amount'), ['amount'], unique=False)
        batch_op.create_index(batch_op.f('ix_transaction_created_at'), ['created_at'], unique=False)
        batch_op.create_index(batch_op.f('ix_transaction_date'), ['date'], unique=False)

    op.create_table('transfer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('source_account', sa.Integer(), nullable=True),
    sa.Column('target_account', sa.Integer(), nullable=True),
    sa.Column('currency', sa.String(length=16), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('amount', sa.Float(precision=64), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['currency'], ['account.currency'], ),
    sa.ForeignKeyConstraint(['source_account'], ['account.id'], ),
    sa.ForeignKeyConstraint(['target_account'], ['account.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('transfer', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_transfer_amount'), ['amount'], unique=False)
        batch_op.create_index(batch_op.f('ix_transfer_created_at'), ['created_at'], unique=False)
        batch_op.create_index(batch_op.f('ix_transfer_date'), ['date'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transfer', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_transfer_date'))
        batch_op.drop_index(batch_op.f('ix_transfer_created_at'))
        batch_op.drop_index(batch_op.f('ix_transfer_amount'))

    op.drop_table('transfer')
    with op.batch_alter_table('transaction', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_transaction_date'))
        batch_op.drop_index(batch_op.f('ix_transaction_created_at'))
        batch_op.drop_index(batch_op.f('ix_transaction_amount'))

    op.drop_table('transaction')
    with op.batch_alter_table('category', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_category_last_modified'))
        batch_op.drop_index(batch_op.f('ix_category_created_at'))

    op.drop_table('category')
    with op.batch_alter_table('account', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_account_last_modified'))
        batch_op.drop_index(batch_op.f('ix_account_created_at'))
        batch_op.drop_index(batch_op.f('ix_account_balance_date'))

    op.drop_table('account')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.drop_index(batch_op.f('ix_user_email'))

    op.drop_table('user')
    # ### end Alembic commands ###
