"""Drop Reference.geninfo_identifier

Revision ID: 3f73b289d4b2
Revises: abe71597ab2c
Create Date: 2016-06-11 14:30:14.353591

"""

from __future__ import unicode_literals

# revision identifiers, used by Alembic.
revision = '3f73b289d4b2'
down_revision = u'abe71597ab2c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.drop_index('ix_references_geninfo_identifier', table_name='references')

    with op.batch_alter_table('references') as batch_op:
        batch_op.drop_column('geninfo_identifier')


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('references', sa.Column('geninfo_identifier', sa.VARCHAR(length=13), autoincrement=False, nullable=True))
    op.create_index('ix_references_geninfo_identifier', 'references', ['geninfo_identifier'], unique=True)
    ### end Alembic commands ###