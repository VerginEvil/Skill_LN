# BLOB handling overview
Tables in the database can contain BLOB columns. BLOBs can contain a lot of data. Therefore BLOB values are not in the record buffer, but the record buffer contains a *BLOB locator* which can be used in a couple of BLOB functions, to read, write and clear the BLOB and to retrieve the size of the BLOB.
A BLOB locator can be retrieved with a db statement (e.g. db.eq()) and with a SQL statement.
A BLOB can only be written to or cleared when the record is locked. The functions *db.blob.append()* and *db.blob.clear()* will promote a delayed lock to a lock in the database.
In cases where the size of the BLOB is unknown, avoid reading the size of the BLOB and then retrieving the entire BLOB at once. This helps avoid memory consumption problems. Instead of retrieving a large chunk of data in one call please consider reading it block by block (e.g. blocksize 4096 or 8192 bytes).

## Restrictions
BLOB operations are executed through the db.blob.* functions, which work on a BLOB locator. For other database operations a number of restrictions apply:

- The SQL processor supports retrieving the BLOB column. A BLOB locator will be returned in the result set, which can be used in the BLOB functions. The SQL processor does not support any other operations on the blob (e.g. no substring, not in the where clause, not in a join)

- Classic QP does not recognize BLOB columns

- BLOB columns can not be part of combined columns or indexes

- It is not possible to have an array column of type BLOB

- It is not possible to define references to or from a BLOB column

- BLOB columns can not be audited

- Tables with BLOB columns can not be mirrored

- When a delayed lock (dlock) is promoted to a lock in the database the delayed lock buffer is compared to the actual values in the database and error EROWCHANGED may be issued. This check does not apply to the BLOB column. Therefore it is recommended to use a database lock rather than a delayed lock for BLOB in cases where this might lead to problems

- The maximum size of a BLOB is determined by the limitations of the underlying RDBMS

## Related topics
- [BLOB handling synopsis](synopsis.md)

- [db.blob.read()](db.blob.read.md)

- [db.blob.read.xml()](db.blob.read.xml.md)

- [db.blob.read.xml.ns()](db.blob.read.xml.ns.md)

- [db.blob.append()](db.blob.append.md)

- [db.blob.append.xml()](db.blob.append.xml.md)

- [db.blob.clear()](db.blob.clear.md)

- [db.blob.size()](db.blob.size.md)
