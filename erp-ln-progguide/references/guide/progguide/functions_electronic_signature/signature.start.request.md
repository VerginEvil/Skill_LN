# signature.start.request()

## Syntax:
`function long signature.start.request( domain ttesg.docm i.docm, [ const string key_field1, const string | long | double key_value1 ], ... )`

## Description
This starts a Signature Request dialog and must be called before performing an action on a document of a specific type (called Document Type) and a list of primary key field/value pairs
A Signature Request dialog only appears if the following applies for the specified Document Type:
1. *In All Companies* checkbox is checked or the current company is in the list of active Companies.
1. *Signature Required* is *Always* or is *Conditional* where all Conditions for Signing have been satisfied.   If all above conditions have been satisfied, the dialog appears with the information as defined for the specified Document Type:
- The Description of the Document Type.
- The Notification of the Document Type if the *Show User Notification* checkbox is checked.
- *Reason for Signing* with an already filled reason if a default reason is defined for the Document Type.
- User Comments if the *Request User Comments* checkbox is checked.   After the current user has successfully signed with Username and Password and the User signed with is allowed to sign, the current values of the Document retrieved based on the specified primary key fields/value pairs and stored in Signed Documents.
The user is allowed to Sign if the *All Users must Sign* checkbox is checked or the user is in the list of active Signers.
After the action has been completed, the Electronic Signature has to be finalized by calling [signature.finish.request()](signature.finish.request.md)

## Arguments
| | | |
|---|---|---|
| `domain ttesg.docm` | `i.docm` |  Type of Document to sign  |
| `[ const string` | `key_field1 ]` |  |
| `[ const string | long | double` | `key_value1 ]` |  |
| `` | `...` |  List of primary key field / value pairs in the format "ppmmm999.ffff", value. In case of array elements, specify the field as "ppmmm999.ffff(element)"  |

## Return values
| | |
|---|---|
| 0 | Successfully signed or signing was not required. |
| -1 | Invalid Username/Password. |
| -2 | Cancelled by User. The User has pressed the Cancel button. |
| -3 | Cannot Authenticate Username/Password. The Authentication Server was not available. |
| -4 | Already authenticating. A Signature Request Dialog is already running elsewhere. |
| -5 | No Reason specified. |
| -6 | User Comments not filled. Only applicable if User Comments is mandatory. |
| -7 | Maximum authentication attempts exceeded. A maximum of 3 failed attempts has been exceeded. |
| -8 | Missing Reasons. No reasons were defined for the specified Document Type. |
| -9 | Missing Notification text. No notification text available for the specified Document Type. Only applicable if the Show Notification checkbox was checked.  |
| -10 | User is not authorized to sign. |
| -11 | Document Transaction failed. The process step, for which a signature was requested, has failed. |
| -12 | Data Integrity Compromised. The data of the Signed Document has been tampered with. |
| -14 | Technical Issue such as cannot create a Signed Document for this request. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types. This function is available from [TIV](../tiv/tiv_overview.md) level 2300.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Example
```

function extern void confirm.shipment()
{
|Precondition: current record of whinh430 is filled with shipment to confirm.

	boolean confirmation.succeeded	| True if confirmation was successful

	if signature.start.request(ttesg.docm.shipmnt.confirm,
			"whinh430.shpm", whinh430.shpm) <> 0 then
		return
	endif

	confirm.shipment(confirmation.succeeded)

	signature.finish.request(confirmation.succeeded)
}
```
Note  After the user has successfully signed, this function stores the current state of the document by calling the function tcgen.dll3000.store.signed.document() of the Electronic Signature Document Definitions DLL (tcgendll3000).

## Related topics
- [Electronic Signature overview](overview.md)
- [Electronic Signature synopsis](synopsis.md)
