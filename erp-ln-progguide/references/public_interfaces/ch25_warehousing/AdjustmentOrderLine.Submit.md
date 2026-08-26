# AdjustmentOrderLine.Submit

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for AdjustmentOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 902-903

```baan
DLL:   whextinhapi
This function is available from     2021.06 (KB2168045  ).
Syntax: long AdjustmentOrderLine.Submit(
domain  tcorno           iAdjustmentOrder,
domain  tcpono           iAdjustmentOrderLine,
domain  tcmcs.str30      iAction,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function will submit a draft version of the adjustment
order line which is being controlled by Object Configuration
Management. The workflow will be started for the adjustment
order line with this function.
Pre:    db.retry.point() must have been set.
This function will read the adjustment order line, so
that is not required from the calling process.
Post:   Commit or abort the transaction
Input:  iAdjustmentOrder                      - Adjustment Order; Mandatory
iAdjustmentOrderLine                          - Adjustment Order Line; Mandatory
iAction                                       - The action to be performed; Mandatory
This action can be one of the default
actions:
Create, Change, Delete.
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                     - Success
<> 0                          - Error
```

## Public Interfaces for ItemWarehouse

The following functions are available: ItemWarehouse.GetHandlingUnitsInUse ItemWarehouse.StartDetail ItemWarehouse.StartOverview
