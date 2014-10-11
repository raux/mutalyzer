"""Fix GRCm38 chromosome accession number versions

Revision ID: 402ff01b0d5d
Revises: ea660b66f26
Create Date: 2014-10-08 15:10:21.522551

"""

from __future__ import unicode_literals

# revision identifiers, used by Alembic.
revision = '402ff01b0d5d'
down_revision = 'ea660b66f26'

from alembic import op
from sqlalchemy import sql
import sqlalchemy as sa


# These accidentally got an extra trailing digit.
ACCESSIONS = ['NC_000067.65',
              'NC_000068.70',
              'NC_000069.60',
              'NC_000070.66',
              'NC_000071.65',
              'NC_000072.60',
              'NC_000073.61',
              'NC_000074.60',
              'NC_000075.60',
              'NC_000076.60',
              'NC_000077.60',
              'NC_000078.60',
              'NC_000079.60',
              'NC_000080.60',
              'NC_000081.60',
              'NC_000082.60',
              'NC_000083.60',
              'NC_000084.60',
              'NC_000085.60',
              'NC_000086.71',
              'NC_000087.74']


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    chromosomes = sql.table('chromosomes',
                            sql.column('accession', sa.String(30)))
    for accession in ACCESSIONS:
        # https://alembic.readthedocs.org/en/latest/ops.html#alembic.operations.Operations.execute
        op.execute(chromosomes.update().where(chromosomes.c.accession == op.inline_literal(accession)).values({'accession': op.inline_literal(accession[:-1])}))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    chromosomes = sql.table('chromosomes',
                            sql.column('accession', sa.String(30)))
    for accession in ACCESSIONS:
        # https://alembic.readthedocs.org/en/latest/ops.html#alembic.operations.Operations.execute
        op.execute(chromosomes.update().where(chromosomes.c.accession == op.inline_literal(accession[:-1])).values({'accession': op.inline_literal(accession)}))
    ### end Alembic commands ###
