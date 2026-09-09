# EngineeringItemRevision.ApproveByEngineering

> Chapter: Chapter 7 Public Interfaces for Engineering Data Management
>
> Group: Public Interfaces for EngineeringItemRevision
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 251-252

```baan
DLL:   tiextedmapi
This function is available from 2024.07 (KB2313151).
Syntax: long EngineeringItemRevision.ApproveByEngineering(
domain  tcitem           iEngineeringItem,
domain  tiedm.revi       iRevision,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function is used to execute the step Approve by
Engineering, for the specified Engineering Item Revision.
Pre:    Retry point must be set.
Post:   Commit or abort the transaction.
Input:  iEngineeringItem        - Engineering Item (Mandatory).
iRevision               - Revision (Mandatory).
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Engineering Item Revision is Approved
by Engineering.
<> 0                    - Engineering Item Revision is not
Approved by Engineering.
```
