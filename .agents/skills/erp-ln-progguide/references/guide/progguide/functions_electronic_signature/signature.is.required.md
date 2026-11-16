# signature.is.required()

## Syntax:
`function boolean signature.is.required( domain ttesg.docm i.docm, long i.compnr )`

## Description
This function tells whether a Signature is required for the document of a specified type (called Document Type) for the specified company.
A Signature is required if:

- An active document exists of the specified type for which the *Signature is Required* option is set

- *In All Companies* checkbox is checked or the current company is in the list of active Companies.

If the above conditions have been satisfied true will be returned else false.
The function can be used to check whether signing will be done by the standard or that application specific variant should be called

## Arguments
| | | |
|---|---|---|
| `domain ttesg.docm` | `i.docm` |  Type of Document to sign  |
| `long` | `i.compnr` |  Company number for which signing requirement should be checked  |

## Return values
| | |
|---|---|
| true | Signing is required. |
| false | Signing is not requied. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2300.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [Electronic Signature overview](overview.md)

- [Electronic Signature synopsis](synopsis.md)
