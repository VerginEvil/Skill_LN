# WarehouseInspection.LinkHandlingUnit

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for WarehouseInspection
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1263-1264

```baan
DLL:   whextinhapi
This function is available from     2021.11 (KB2209571  ).
Syntax: long WarehouseInspection.LinkHandlingUnit(
domain  tcorno           iInspection,
domain  tcpono           iInspectionSequence,
domain  whhuid           iHandlingUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface supports linking of a handling unit in
stock to an existing Inventory Inspection.
Warehouse Inspection must be of type Inventory Inspection.
Handling unit must have status In Stock.
The result of this public interface will be that the
iHandlingUnit is linked to the Warehouse Inspection.
The iHandlingUnit will get status To be Inspected.
Stock point details of the handling unit will be added as
inspection lines to the Inventory Inspection.
Pre:    db.retry.point() is set.
Post:   commit.transaction() / abort.transaction()
Input:  iInspection                           - Inspection Number (mandatory)
iInspectionSequence                           - Inspection Sequence (mandatory)
iHandlingUnit                                 - Handling Unit (mandatory)
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
