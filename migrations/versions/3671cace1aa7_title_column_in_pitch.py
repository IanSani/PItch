"""title column in pitch
Revision ID: 3671cace1aa7
Revises: 91418a3b5b22
Create Date: 2019-04-25 10:40:47.381851
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3671cace1aa7'
down_revision = '91418a3b5b22'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(length=255), nullable=True),
    sa.Column('date_posted', sa.DateTime(timezone=250), nullable=True),
    sa.Column('pitches_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitches_id'], ['pitches.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('comment_vote')
    op.add_column('pitches', sa.Column('title', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'title')
    op.create_table('comment_vote',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('comment', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('date_posted', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('pitches_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['pitches_id'], ['pitches.id'], name='comment_vote_pitches_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='comment_vote_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='comment_vote_pkey')
    )
    op.drop_table('comments')
    # ### end Alembic commands ###
