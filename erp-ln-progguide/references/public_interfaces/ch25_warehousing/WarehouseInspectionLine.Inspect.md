# WarehouseInspectionLine.Inspect

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for WarehouseInspectionLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1281-1282

```baan
DLL:   whextinhapi
This function is available from 2021.09 (KB2202105).
Syntax: long WarehouseInspectionLine.Inspect(
domain  tcorno           iInspection,
domain  tcpono           iInspectionSequence,
long             iInspectionLine,
domain  tcqst1           iApprovedQuantity,
domain  tccuni           iApprovalUnit,
domain  tcqiv1           iDestroyedQuantity,
domain  tccdis           iDestroyReason,
domain  tcqst1           iRejectedQuantity,
domain  tccuni           iRejectUnit,
domain  tccdis           iRejectReason,
domain  tcqst1           iScrappedQuantity,
domain  tccdis           iScrapReason,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function updates the inspection results of a specific
Warehouse Inspection Line which is not linked to a handling unit.
The Warehouse Inspection should have status Open or In Process
and not reside in a WMS-controlled warehouse.
This function does not process the inspection results.
For processing, use WarehouseInspection.Process
Pre:    db.retry.point() is set.
Post:   commit.transaction() / abort.transaction()
Input:  iInspection             - Inspection Number (mandatory)
iInspectionSequence     - Inspection Sequence (mandatory)
iInspectionLine         - Inspection Line (mandatory)
iApprovedQuantity       - Approved quantity
iApprovalUnit           - Approval Unit (mandatory if approved
quantity is greater than zero).
If some quantity is destroyed, the
approval unit must be in inventory unit.
iDestroyedQuantity      - Destroyed Quantity. Destroyed goods
are part of the Approved Quantity and is
not allowed for Outbound Inspections.
iDestroyReason          - Destroy Reason (mandatory if destroyed
quantity is greater than zero).
Reason must be of type 'Destroyed during
inspection'.
iRejectedQuantity       - Rejected Quantity
iRejectUnit             - Rejection Unit (mandatory if rejected
quantity is greater than zero).
iRejectReason           - Reject Reason (mandatory if rejected
quantity is greater than zero).
Reason must be of type 'Rejection of Goods'.
iScrappedQuantity       - Scrapped Quantity (in Rejection Unit).
Scrapped quantity is part of Rejected quantity.
iScrapReason            - Scrap Reason (mandatory if scrapped
quantity is greater than zero).
Reason must be of type 'Disposition'.
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```
