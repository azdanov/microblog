"""posts table

Revision ID: 7ca004cb303a
Revises: f9a9c741f0d6
Create Date: 2019-10-26 05:05:45.734292

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "7ca004cb303a"
down_revision = "f9a9c741f0d6"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "post",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("body", sa.String(length=140), nullable=True),
        sa.Column("timestamp", sa.DateTime(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_post_timestamp"), "post", ["timestamp"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_post_timestamp"), table_name="post")
    op.drop_table("post")
    # ### end Alembic commands ###
