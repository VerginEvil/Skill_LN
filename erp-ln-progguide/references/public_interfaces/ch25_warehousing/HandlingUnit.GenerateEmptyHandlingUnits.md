# HandlingUnit.GenerateEmptyHandlingUnits

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for HandlingUnit
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1046-1047

```baan
DLL:   whextwmdapi
This function is available from 2021.04 (KB2181351).
Syntax: long HandlingUnit.GenerateEmptyHandlingUnits(
domain  whhuid           iHandlingUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface will generate empty handling units for the
given iHandlingUnit. This public interface will only generate
new empty handling units when the following conditions are met:
- Package Definition must be filled on the iHandlingUnit
- Handling Unit Template used for the Package Definition should
have nodes which use the fill up with empty packages enabled.
- iHandlingUnit should not be a multi item handling unit
- iHandlingUnit should have status Projected or Staged
- iHandlingUnit should have child Handling Units
- iHandlingUnit should not be empty itself
The functionality will make sure that based on the handling unit
template, the packaging structure is stabilized. For example,
a pallet can contain 4 crates, when only 3 crates are put on a
pallet, it can be required to add an empty crate (no items are
inside) to form a stable packaging structure.
Pre:    db.retry.point()
Post:   abort.transaction() or commit.transaction()
Input:  iHandlingUnit   - Handling Unit for which empty handling units
must be created (Mandatory)
Output: oExceptionMessage - The last message if any message is found. If
more than one  message is given, these are present in
the oExceptionID.
oExceptionID - An ID that refers to all error information. Use
the functions in Exception to get all relevant
information.
Return: 0       - Handling Unit is stabilized
<> 0    - Error
```
