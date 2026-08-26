# signed.document.add.field.desc()

## Syntax:
`function long signed.document.add.field.desc( long i.document.xml, const string i.table.field.name, const string i.key.reference, const string i.label, const string i.desc, [ long element ] )`

## Description
This adds an additional description to a table field in a Signed Document XML.

## Arguments
| | | |
|---|---|---|
| `long` | `i.document.xml` |  the Signed Document XML  |
| `const string` | `i.table.field.name` |  the name of the table field(e.g. "whinh430.wdep") to which the description is added in Signed Document XML.  |
| `const string` | `i.key.reference` |  the key reference to which the additional field description is added.  |
| `const string` | `i.label` |  the label for the additional description to add to the field.  |
| `const string` | `i.desc` |  the additional description to add to the field.  |
| `[ long` | `element ]` |  Optional element number of the table field to which the additional description is added, use this in case of array elements.  |

## Return values
| | |
|---|---|
| 0 | Additional description successfully added to the specified field in the Signed Document XML. |
| -1 | Invalid Signed Document XML. |
| -2 | Empty Table Field Name. |
| -3 | Invalid Table Field Name. |
| -4 | Table Field with specified reference cannot be found in the Signed Document XML. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2300.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Electronic Signature overview](overview.md)
- [Electronic Signature synopsis](synopsis.md)
