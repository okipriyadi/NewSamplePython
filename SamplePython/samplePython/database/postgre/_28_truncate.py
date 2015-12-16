"""
The PostgreSQL TRUNCATE TABLE command is used to delete complete data from an existing table.
You can also use DROP TABLE command to delete complete table but it would remove complete table structure
from the database and you would need to re-create this table once again if you wish to store some data.
It has the same effect as an DELETE on each table, but since it does not actually scan the tables, it is faster.
Furthermore, it reclaims disk space immediately, rather than requiring a subsequent VACUUM operation. This is
most useful on large tables.

The basic syntax of TRUNCATE TABLE is as follows:
====================================================================================+
TRUNCATE TABLE table_name;
====================================================================================+

"""