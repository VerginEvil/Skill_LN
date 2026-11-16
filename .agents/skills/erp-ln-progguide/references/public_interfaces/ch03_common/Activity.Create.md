# Activity.Create

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Activity
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 146-148

```baan
DLL:   tcextcomapi
This function is available from 2026.09 (KB3674937).
Syntax: long Activity.Create(
domain  tccom.actp       iActivityType,
boolean          iSetLinkedActivity,
domain  tccom.acty       iLinkedActivity,
boolean          iSetSubject,
domain  tcdscf           iSubject mb,
boolean          iSetBusinessPartner,
domain  tccom.bpid       iBusinessPartner,
boolean          iSetContact,
domain  tccom.ccnt       iContact,
boolean          iSetAssignedTo,
domain  tcemno           iAssignedTo,
boolean          iSetOwner,
domain  tcemno           iOwner,
boolean          iSetPriority,
domain  tccom.acpr       iPriority,
boolean          iSetSensitivity,
domain  tccom.sens       iSensitivity,
boolean          iSetInformation,
domain  tctxtn           iInformation,
boolean          iSetGUID,
domain  tcguid           iGUID,
boolean          iSetBusinessObjectType,
domain  tccom.bota       iBusinessObjectType,
boolean          iSetBusinessObject,
domain  tcprbo           iBusinessObject,
boolean          iSetBusinessObjectLineRef,
domain  tcborf           iBusinessObjectLineRef,
boolean          iSetBusinessObjectDetailRef,
domain  tcborf           iBusinessObjectDetailRef,
domain  tccom.actp       iSourceActivityType,
ref     domain  tccom.acty       oActivity,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function creates an Activity (tccom600).
Most fields have an accompanying boolean "set" argument.
When the boolean is true the field value will be used,
otherwise the field will not be set and the default logic
from the DAL will be applied.
Pre:    Caller must set retry-point.
Post:   Caller must commit/abort transaction.
Input:
iActivityType           - Activity Type  (mandatory)
iSetLinkedActivity      - Set Linked Activity (true/false)
iLinkedActivity         - Linked Activity
iSetSubject             - Set Subject (true/false)
iSubject                - Subject
iSetBusinessPartner     - Set Business Partner (true/false)
iBusinessPartner        - Business Partner
iSetContact             - Set Contact (true/false)
iContact                - Contact
iSetAssignedTo          - Set Assigned To (true/false)
iAssignedTo             - Assigned To (Employee)
iSetOwner               - Set Owner (true/false)
iOwner                  - Owner (Employee)
iSetPriority            - Set Priority (true/false)
iPriority               - Priority
iSetSensitivity         - Set Sensitivity (true/false)
iSensitivity            - Sensitivity
iSetInformation         - Set Information (true/false)
iInformation            - Information (Text Number)
iSetGUID                - Set GUID (true/false)
iGUID                   - GUID
iSetBusinessObjectType  - Set Business Object Type (true/false)
iBusinessObjectType     - Business Object Type
iSetBusinessObject      - Set Business Object (true/false)
iBusinessObject         - Business Object
iSetBusinessObjectLineRef
- Set Business Object Line Reference
(true/false)
iBusinessObjectLineRef  - Business Object Line Reference
iSetBusinessObjectDetailRef
- Set Business Object Detail Reference
(true/false)
iBusinessObjectDetailRef- Business Object Detail Reference
iSourceActivityType     - Source Activity Type (for duplicating
attendees from linked activity)
iSourceActivityType is only relevant
when iSetLinkedActivity = true
Output: oActivity               - The created Activity ID
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Activity created successfully.
<> 0                    - Otherwise.
```
