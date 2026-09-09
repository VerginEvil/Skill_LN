# cmf.addObjectToMessage()

## Syntax:
`#include <bic_cmf>`
`function long cmf.addobjecttomessage( long oid, long mid, string class(100) )`

## Description
The object identified by *oid* is added to the message object identified by *mid*. The class of this message is set to the *string class* (mandatory attribute for a message: for example CMF.TASK for tasks, CMF.APPOINTMENT for appointments and so on). The object is written to a temporary file with extension.xml, which is placed in the current working directory. This file is added as an attachment to the message object. The body attribute of this attachment is set to true, the mimetype is set to application/xml and the delete attribute is set to true. All attachments currently attached to the task are also attached to the message object. Finally the object identified by *oid* is deleted (because changes in this object are not reflected anymore in the message object).
Note: If an error is returned, the object identified by oid is not deleted

## Arguments
| | | |
|---|---|---|
| `long` | `oid` |  Object identification.  |
| `long` | `mid` |  Message object identification.  |
| `string` | `class(100)` |  Mandatory attribute for a message: for example CMF.TASK for tasks, CMF.APPOINTMENT for appointments and so on. For more information see cmf.setClasscmf.setClass.  |

## Return values
| | |
|---|---|
| 0 | Success. |
| -1 | General error (check logfiles). |
| -2 | Oid or mid are not valid xml object id's. |
| -3 | Class argument empty. |
| -4 | Object could not be written to file. |

## Context
This function is implemented in the 4GL Engine and can be used in all script types.
This function is marked as 'untrusted' and can therefore not be used in custom objects in a cloud-ready environment. See section about [managed execution](../misc/managed_execution.md) for more information.

## Related topics
- [eMessage Connector overview](overview.md)

- [eMessage Connector synopsis](synopsis.md)

- [eMessage Connector examples](examples.md)
