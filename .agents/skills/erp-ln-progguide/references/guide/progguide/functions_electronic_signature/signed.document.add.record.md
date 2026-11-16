# signed.document.add.record()

## Syntax:
`function long signed.document.add.record( long i.document.xml, const string i.table.name )`

## Description
This adds the table fields and their current values of the specified table to a Signed Document XML.

## Arguments
| | | |
|---|---|---|
| `long` | `i.document.xml` |  the Signed Document XML  |
| `const string` | `i.table.name` |  the table name (e.g. "whinh430") for which all the fields and their current values are added to the Signed Document XML.  |

## Return values
| | |
|---|---|
| 0 | Table fields and values successfully added to Signed Document XML. |
| -1 | Invalid Signed Document XML. |
| -2 | Invalid Table Name. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2300.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Electronic Signature overview](overview.md)

- [Electronic Signature synopsis](synopsis.md)
