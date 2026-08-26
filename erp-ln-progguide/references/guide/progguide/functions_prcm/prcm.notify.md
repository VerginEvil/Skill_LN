# prcm.notify()

## Syntax:
`function void prcm.notify( const string subject, [ string aspect(32), long data ] )`

## Description
Is called by a subject process to notify other processes that it has changed. Optionally, an aspect can be specified to indicate what aspect of the subject process has changed.
It is also possible to pass some data to the observer processes in the form of an XML document. Observer processes then have read-only access to this XML document.

## Arguments
| | | |
|---|---|---|
| `const string` | `subject` |  The subject that has changed. This can be freely defined.  |
| `[ string` | `aspect(32) ]` |  Optional aspect of the subject that has changed. This can be freely defined.  |
| `[ long` | `data ]` |  Optional xml node containing data that observers might be interested in. The contents of the XML document can be freely defined. From [Tools Interface Version (TIV)](../tiv/tiv_overview.md) 2000, the XML structure is duplicated to the PRCM process. In older versions, only a reference to the XML is sent to the other processes.  |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
Note  Do not call [prcm.notify()](prcm.notify.md) for the maintable in the *after.update.db.commit* section or the [after.commit.transaction()](../functions_dal/after.commit.transaction.md) hook of the DAL of the maintable, as this interferes with the automatic notification of the 4GL engine.

## Related topics
- [Process Change Manager overview](overview.md)
- [Process Change Manager synopsis](synopsis.md)
- [Process Change Manager Code Examples](examples.md)
