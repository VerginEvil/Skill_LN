# ServiceQuote.Process

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceQuote
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1479-1480

```baan
DLL:   tsexteppapi
This function is available from 2021.12 (KB2215314).
Syntax: long ServiceQuote.Process(
domain  tcorno           iQuote,
domain  tcpono           iQuoteRevision,
domain  tcseri           iServiceOrderSeries,
domain  tcseri           iMaintenanceSalesOrderSeries,
domain  tcyesno          iATPCheck,
domain  tcyesno          iCheckPlannedInventory,
domain  tcyesno          iCheckInventoryOnHand,
domain  tcyesno          iSkipBlockedInventory,
domain  tcyesno          iBlockInCaseOfInventoryShortage,
domain  tsmdm.scin       iScopeOfInventoryCheck,
domain  tcyesno          iUpdatePlannedDeliveryTimeMaterialLine,
domain  tcyesno          iUpdateQuoteLinesWithLastPlannedMaterialLine,
domain  tcyesno
iSynchronizeQuoteLinesWithLastPlannedMaterialLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function handles the processing of a service quote to
a service order or maintenance sales order.
Based on the given options/settings for processing the quote,
additional checks related to inventory availability are done.
Note:
- If a part maintenance line is created, no work order will be
created, regardless the value of the related maintenance
sales control parameter.
Pre     : a db.retry.point() must have been specified.
Post    : an abort.transaction() or commit.transaction() must be
executed.
Method: 'WorkOrder.CreateMSO' of BDE 'WorkOrder' can be used
to create the related work order.
Input:  iQuote  -
Service Quote (mandatory)
iQuoteRevision  -
Service Quote Revision (optional)
iServiceOrderSeries     -
Service Order Series (not mandatory)
iMaintenanceSalesOrderSeries    -
Maintenance Sales Order Series (not mandatory)
iATPCheck       -
Perform ATP check (mandatory Yes/No)
iCheckPlannedInventory  -
Check Planned Available Inventory (mandatory Yes/No)
iCheckInventoryOnHand   -
Check On Hand Inventory (mandatory Yes/No)
iSkipBlockedInventory   -
Skip Blocked Inventory (mandatory Yes/No)
iBlockInCaseOfInventoryShortage -
Block Planning or Releasing of Orders with Shortages
(mandatory Yes/No)
iScopeOfInventoryCheck  -
Scope of Inventory Check (mandatory)
Possible values:
- current warehouse only
- all warehouses in planning cluster
iUpdatePlannedDeliveryTimeMaterialLine  -
Update Planned Delivery Time of Material Lines
(mandatory Yes/No)
iUpdateQuoteLinesWithLastPlannedMaterialLine    -
Update Quote Lines with Latest Planned
Material Line (mandatory Yes/No)
iSynchronizeQuoteLinesWithLastPlannedMaterialLine       -
Synchronize Quote lines with Latest Planned
Material Line
(mandatory Yes/No)
Output:
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0       - process succesful
<> 0    - Error during process occurred
```
