# set.transaction.readonly()

## Syntax:
`function long set.transaction.readonly( )`

## Description
This defines a transaction as read only. The transaction can only read records (without locks) from the database; it cannot update the database.
When included, this function must be the first command of a transaction. So, you must include it either at the start of the program or immediately following a [commit.transaction()](commit.transaction.md) or [abort.transaction()](abort.transaction.md) call.
Because it is not possible to update the database in a read-only transaction, you can use only the following database calls in the transaction:
db.first() db.lt()
db.last() db.le()
db.next() db.set.to.default()
db.prev() db.change.order()
db.gt() db.indexinfo()
db.ge() db.nr.indices()
db.eq() db.nr.rows()
db.cur() db.row.length()
db.bind() db.record.to.columns()
db.unbind() db.columns.to.record()
db.error()

## Context
This function is implemented in the porting set and can be used in all script types.

## Related topics
- [Database operations overview](overview.md)

- [Database operations synopsis](synopsis.md)
