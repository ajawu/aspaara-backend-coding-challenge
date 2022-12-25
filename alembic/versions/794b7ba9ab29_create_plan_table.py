"""create plan table

Revision ID: 794b7ba9ab29
Revises:
Create Date: 2022-12-25 20:27:59.084748

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "794b7ba9ab29"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "plan",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("original_id", sa.Integer(), nullable=False),
        sa.Column("talent_id", sa.String(), nullable=True),
        sa.Column("talent_name", sa.String(), nullable=True),
        sa.Column("talent_grade", sa.String(), nullable=True),
        sa.Column("booking_grade", sa.String(), nullable=True),
        sa.Column("operating_unit", sa.String(), nullable=False),
        sa.Column("office_city", sa.String(), nullable=True),
        sa.Column("office_postal_code", sa.String(), nullable=False),
        sa.Column("job_manager_name", sa.String(), nullable=True),
        sa.Column("job_manager_id", sa.String(), nullable=True),
        sa.Column("total_hours", sa.Float(), nullable=False),
        sa.Column("start_date", sa.DateTime(), nullable=False),
        sa.Column("end_date", sa.DateTime(), nullable=False),
        sa.Column("client_name", sa.String(), nullable=True),
        sa.Column("client_id", sa.String(), nullable=False),
        sa.Column("industry", sa.String(), nullable=True),
        sa.Column("required_skills", sa.String(), nullable=True),
        sa.Column("optional_skills", sa.String(), nullable=True),
        sa.Column("is_unassigned", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_plan_id"), "plan", ["id"], unique=False)
    op.create_index(op.f("ix_plan_original_id"), "plan", ["original_id"], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_plan_original_id"), table_name="plan")
    op.drop_index(op.f("ix_plan_id"), table_name="plan")
    op.drop_table("plan")
    # ### end Alembic commands ###
