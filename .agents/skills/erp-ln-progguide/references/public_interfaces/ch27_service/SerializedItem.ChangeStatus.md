# SerializedItem.ChangeStatus

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for SerializedItem
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1355-1356

```baan
DLL:   tsextcfgapi
This function is available from 2025.10 (KB3624238).
Syntax: long SerializedItem.ChangeStatus(
domain  tcitem           iItem,
domain  tcibd.sern       iSerialNumber,
domain  tscfg.cfst       iChangeToStatus,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.   : This function changes the status of a Serialized Item and
therefore provides the same functionality as session
tscfg2230m000.
The following new statuses are supported:
- Active
- Defective
- Working Condition
- To be Recycled
- Removed
This function can only be used if the current status of the
serialized item is not Startup, Revision or Superseded,
because this functionality is only used to set a physical
status value. The administrative status can be set in
tscfg2100m000.
When changing the status of a Serialized Item to Removed, the
item will automatically be removed from the Installation Group.
Pre     : A db.retry.point() must have been specified.
Post    : An abort.transaction() or commit.transaction() must be
executed.
Input   : - iItem               - The Item of which the status must be
changed.
- iSerialNumber       - The Serial Number of which the status
must be changed; Mandatory
- iChangeToStatus     - The Status that the serialized item
must be changed to; Mandatory
Allowed statuses:
- Active
- Defective
- Working Condition
- To be Recycled
- Removed
Output  : - ExceptionMessage    - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
- oExceptionID        - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return  : 0                     - No error
<> 0                  - An error occurred
```
