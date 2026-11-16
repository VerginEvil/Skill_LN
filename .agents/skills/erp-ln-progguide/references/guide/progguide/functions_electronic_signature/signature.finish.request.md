# signature.finish.request()

## Syntax:
`function long signature.finish.request( boolean i.succeeded )`

## Description
Finalizes the signing of a Document that was initiated with [signature.start.request()](signature.start.request.md).
This function is called after the form command has been executed. When called, the function retrieves the current values of the Document and store it as the after state of the Signed Document.

## Arguments
| | | |
|---|---|---|
| `boolean` | `i.succeeded` |  Indicates if the form command was executed successfully.  |

## Return values
| | |
|---|---|
| 0 | Successfully signed or signing was not required. |
| -1 | Invalid Username/Password. |
| -2 | Cancelled by User. The User has pressed the Cancel button. |
| -3 | Cannot Authenticate Username/Password. The Authentication Server was not available. |
| -4 | Already authenticating. A Signature Request dialog is already running elsewhere. |
| -5 | No Reason specified. |
| -6 | User Comments not filled. Only applicable if User Comments is mandatory. |
| -7 | Maximum authentication attempts exceeded. A maximum of 3 failed attempts has been exceeded. |
| -8 | Missing Reasons. No reasons were defined for the specified Document Type. |
| -9 | Missing Notification text. No notification text available for the specified Document Type. Only applicable if the Show Notification checkbox was checked. |
| -10 | User is not authorized to sign. |
| -11 | Document Transaction failed. The process step, for which a signature was requested, has failed. |
| -12 | Data Integrity Compromised. The data of the Signed Document has been tampered with. |
| -14 | Technical Issue such as cannot create a Signed Document for this request. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2300.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.
Note  This function stores the current state of the document by calling the function tcgen.dll3000.store.signed.document() of the Electronic Signature Document Definitions DLL (tcgendll3000).

## Related topics
- [Electronic Signature overview](overview.md)

- [Electronic Signature synopsis](synopsis.md)
