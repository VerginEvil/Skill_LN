# EngineeringItemRevision.ApproveByProduction

> Chapter: Chapter 7 Public Interfaces for Engineering Data Management
>
> Group: Public Interfaces for EngineeringItemRevision
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 250-251

```baan
DLL:   tiextedmapi
This function is available from     2023.12 (KB2300180  ).
Syntax: long EngineeringItemRevision.ApproveByProduction(
domain  tcitem           iEngineeringItem,
domain  tibmrv           iRevision,
boolean          iCopyRelationsFromPreviousRevision,
boolean          iOverwriteDescription,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function is used to approve by production the specified
Engineering Item Revision.
Note that this function will continue processing when:
-                       no relation is present for the Item Engineering Revision
-                       the Effective Date of the Item Engineering Revision is
before the current date.
Also note that this function will do abort.transaction() in some
cases.
Pre:    Retry point must be set.
Post:   Commit or abort the transaction.
Input:  iEngineeringItem                      - Engineering Item (Mandatory).
iRevision                                     - Revision (Mandatory).
iCopyRelationsFromPreviousRevision
-                                               Control for copying relations from
previous revision.
iOverwriteDescription                         - Control for overwriting descriptions
and/or search keys.
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Engineering Item Revision is Approved
by Production.
<> 0                                          - Engineering Item Revision is not
Approved by Production.
```
