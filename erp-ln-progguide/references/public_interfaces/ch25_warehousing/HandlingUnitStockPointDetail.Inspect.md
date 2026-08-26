# HandlingUnitStockPointDetail.Inspect

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for HandlingUnitStockPointDetail
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1277-1279

```baan
DLL:   whextwmdapi
This function is available from     2021.09 (KB2202105  ).
Syntax: long HandlingUnitStockPointDetail.Inspect(
domain  whhuid           iHandlingUnit,
domain  tcmcs.long       iDistributionSequence,
domain  tccuni           iStorageUnit,
domain  tcqst1           iApprovedQuantity,
domain  tcqiv1           iDestroyedQuantity,
domain  tccdis           iDestroyReason,
domain  tcqst1           iRejectedQuantity,
domain  tccdis           iRejectReason,
domain  tcqst1           iScrappedQuantity,
domain  tccdis           iScrapReason,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function updates the inspection results of a specific
Handling Unit Stock Point Detail                       - Distribution Sequence.
The related warehouse inspection of the Handling Unit should
have status Open or In Process and not reside in a
WMS                      -controlled warehouse.
This function must only be called for bottom handling units
(not allowed for handing unit having child handling unit(s)).
This function can also not be used for warehouse inspections
which are blocked by a QM Order Inspection.
This function does not process the inspection results.
For processing, use WarehouseInspection.Process
Pre:    db.retry.point() is set.
Post:   commit.transaction() / abort.transaction()
Input:  iHandlingUnit                         - Handling Unit (mandatory)
iDistributionSequence                         - Handling Unit Stock Point Detail
Distribution Sequence (mandatory)
iStorageUnit                                  - Storage Unit (mandatory)
iApprovedQuantity                             - Approved quantity (in storage unit)
iDestroyedQuantity                            - Destroyed Quantity (in inventory unit)
Destroyed goods are part of the Approved
Quantity and must be expressed in
inventory unit and is not allowed for
Outbound Inspections.
iDestroyReason                        -        Destroy Reason (mandatory if destroyed
quantity is greater than zero).
Reason must be of type 'Destroyed during
inspection'.
iRejectedQuantity                             - Rejected Quantity (in storage unit)
iRejectReason                                 - Reject Reason (mandatory if rejected
quantity is greater than zero).
Reason must be of type 'Rejection of Goods'.
iScrappedQuantity                             - Scrapped Quantity (in storage unit)
Scrapped quantity is part of Rejected quantity.
iScrapReason                                  - Scrap Reason (mandatory if scrapped
quantity is greater than zero).
Reason must be of type 'Disposition'.
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
