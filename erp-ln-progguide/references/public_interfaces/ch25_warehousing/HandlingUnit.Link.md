# HandlingUnit.Link

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for HandlingUnit
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1051-1051

```baan
DLL:   whextwmdapi
This function is available from 2020.08 (KB2131012).
Syntax: long HandlingUnit.Link(
domain  whhuid           iChildHandlingUnit,
domain  whhuid           iParentHandlingUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface will compose handling unit structure by
means of linking iChildHandlingUnit to iParentHandlingUnit.
Input data will be verified as follows:
- Both iChildHandlingUnit and iParentHandlingUnit must be filled;
- Both iChildHandlingUnit and iParentHandlingUnit must be present
in the table Handling Units (whwmd530);
- iChildHandlingUnit and iParentHandlingUnit cannot have the same
value;
- Status of iChildHandlingUnit cannot be equal to:
Closed
Frozen
Partially Frozen
Confirming
Shipped
InTransit
- Status of iParentHandling.unit must be Inactive or equal to
the status of iChildHandlingUnit. Combination of handling units
with status Projected and Staged is also allowed.
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iChildHandlingUnit - Child Handling Unit (Mandatory)
iParentHandlingUnit - Parent Handling Unit (Mandatory)
Output: oExceptionMessage - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0       - Handling Unit structure is composed successfully
<> 0    - Error
```
