# Activities.StartOverview

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for Activities
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 144-145

```baan
DLL:   tcextcomapi
This function is available from     2026.04 (KB3665487  ).
Syntax: long Activities.StartOverview(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcemno           iFilterEmployee,
domain  tccom.ccnt       iFilterContact,
domain  tccom.bpid       iFilterBusinessPartner,
domain  tcyesno          iFilterOpenActivitiesOnly,
domain  tcyesno          iFilterToggleAssignedAttendActivities,
domain  tccom.acty       iActivity,
domain  tccom.bpid       iBusinessPartner,
domain  tccom.ccnt       iContact,
domain  tccom.bota       iBusinessObjectType,
domain  tcprbo           iBusinessObject,
domain  tcborf           iBusinessObjectLineReference,
domain  tcborf           iBusinessObjectDetailReference,
domain  tcguid           iUniqueIdentifier,
domain  tcdate           iDueDate,
domain  tccom.actp       iActivityType,
ref     domain  tccom.acty       oActivity,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface starts the overview session
"Activities (tccom6100m000)"
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Specifies the start filter that is to be applied to the
started session.
Possible values are:
"" (Session has no start filter)
iSessionIndex
Specifies the session index that is to be used. Please
be aware that the iStartFilter will overrule the index
passed in this argument. So when not using a startfilter
the session index will match the value of this variable.
Possible Values are: 1 to 6.
Note:                               - Session Index 7 and Session Index 8 are not
available on the session.
iQueryExtend
Optional
A specific query to be used when zooming to this session.
iFilterEmployee                                       - Employee Filter
iFilterContact                                        - Contact Filter
iFilterBusinessPartner                                - Business Partner Filter
iFilterOpenActivitiesOnly                             - Open Activities Only Filter
iFilterToggleAssignedAttendActivities
-                                                       Toggle Assigned/Attend
Activities Filter
iActivity                                             - Activity
iBusinessPartner                                      - Business Partner
iContact                                              - Contact
iBusinessObjectType                                   - Business Object Type
iBusinessObject                                       - Business Object
iBusinessObjectLineReference                          - Business Object Line Reference
iBusinessObjectDetailReference                        - Business Object Detail
Reference
iUniqueIdentifier                                     - Unique Identifier
iDueDate                                              - Due Date
iActivityType                                         - Activity Type
Output: oActivity                                     - Selected Activity
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - Otherwise.
```

## Public Interfaces for Activity

The following functions are available: Activity.Create
