"""initial migration

Revision ID: abebf66b7934
Revises: 
Create Date: 2025-01-03 16:23:08.281539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abebf66b7934'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('flight',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('takeoff_time', sa.Time(), nullable=False),
    sa.Column('landing_time', sa.Time(), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('takeoff_location', sa.String(length=100), nullable=False),
    sa.Column('landing_location', sa.String(length=100), nullable=False),
    sa.Column('takeoff_altitude', sa.Float(), nullable=True),
    sa.Column('max_altitude', sa.Float(), nullable=True),
    sa.Column('distance_covered', sa.Float(), nullable=True),
    sa.Column('temperature', sa.Integer(), nullable=True),
    sa.Column('wind_speed', sa.Float(), nullable=True),
    sa.Column('wind_direction', sa.String(length=50), nullable=True),
    sa.Column('weather_conditions', sa.Text(), nullable=True),
    sa.Column('equipment_used', sa.String(length=200), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('gps_track', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('flight')
    # ### end Alembic commands ###
