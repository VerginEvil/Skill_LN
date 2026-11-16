# signed.document.add.extra.field()

## Syntax:
`function long signed.document.add.extra.field( long i.document.xml, const string i.table.name, const string i.key.reference, const string i.label, const string i.value )`

## Description
This adds a field and its value to a table in a Signed Document XML.

## Arguments
| | | |
|---|---|---|
| `long` | `i.document.xml` |  the Signed Document XML  |
| `const string` | `i.table.name` |  the table name (e.g. "whinh430") to which the extra field is added in a Signed Document XML.  |
| `const string` | `i.key.reference` |  the key reference to which the extra table field is added.  |
| `const string` | `i.label` |  the description for the extra field that is added.  |
| `const string` | `i.value` |  the value for the extra field that is added.  |

## Return values
| | |
|---|---|
| 0 | Extra field successfully added to Signed Document XML. |
| -1 | Invalid Signed Document XML. |
| -2 | Empty Table Name. |
| -4 | Table with specified reference cannot be found in the Signed Document XML. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2300.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Electronic Signature overview](overview.md)

- [Electronic Signature synopsis](synopsis.md)
