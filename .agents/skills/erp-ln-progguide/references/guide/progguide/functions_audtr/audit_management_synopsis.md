# Audit management synopsis
For a good overview of the relations between the audit management functions see the [Relations between the functions](#flow).

## Include files for audit management functions
```

#include <bic_audhdr.h>
#include <bic_audlib>
```

## Selecting transaction and action data
```
long
```
```
bool
```
```
long
```
```
long
```
| | | |
|---|---|---|
|  | [aud.select.transactions()](aud.select.transactions.md) | `(long nr.tables, const string table.codes(,), const long companies(), const string selection.criteria, ref long selection.id)` |
|  | [aud.audit.is.on.for.table()](aud.audit.is.on.for.table.md) | `(const string table.code(), long company)` |
|  | [aud.get.next.transaction()](aud.get.next.transaction.md) | `(long selection.id, long number.of.retries, long retry.interval, ref string transaction.id, ref long commit.time, ref string session, ref string user)` |
|  | [aud.get.next.action()](aud.get.next.action.md) | `(long selection.id, ref long table.id, ref long company, ref string table.code, ref bool meta.data.changed, ref long current.action.number, ref string action.type)` |

## Handling meta data
```
long
```
```
long
```
```
long
```
```
void
```
| | | |
|---|---|---|
|  | [aud.get.number.of.fields()](aud.get.number.of.fields.md) | `(long selection.id, long table.id, ref long number.of.fields)` |
|  | [aud.get.field.list()](aud.get.field.list.md) | `(long selection.id, long table.id, ref string field.names(,))` |
|  | [aud.get.field.ids()](aud.get.field.ids.md) | `(long selection.id, long table.id, long number.of.fields, const string field.names(,), ref long field.ids())` |
|  | [aud.get.field.info()](aud.get.field.info.md) | `(long selection.id, long table.id, long field.id, ref long field.depht, ref long field.type, ref long field.length)` |

## Retrieving field information for a database action
```
string
```
```
void
```
```
void
```
| | | |
|---|---|---|
|  | [aud.get.field.status()](aud.get.field.status.md) | `(long selection.id, long table.id, long field.id)` |
|  | [aud.put.old.field.value](aud.put.old.field.value.md) | `(long pid, string variable.name, long selection.id, long table.id, long field.id, long element [, bool endian] )` |
|  | [aud.put.new.field.value](aud.put.old.field.value.md) | `(long pid, string variable.name, long selection.id, long table.id, long field.id, long element [, bool endian] )` |

## Closing the selection of transaction data
```
long
```
| | | |
|---|---|---|
|  | [aud.close.selection()](aud.close.selection.md) | `(long selection.id)` |

## Relations between the functions

## Related topics
- [Audit management overview](audit_management_overview.md)

- [Audit management examples](audit_management_examples.md)
