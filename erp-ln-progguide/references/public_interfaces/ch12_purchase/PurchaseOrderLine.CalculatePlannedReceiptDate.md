# PurchaseOrderLine.CalculatePlannedReceiptDate

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 455-456

```baan
DLL:   tdextpurapi
This function is available from 2021.11 (KB2213129).
Syntax: long PurchaseOrderLine.CalculatePlannedReceiptDate(
domain  tcorno           iOrderNumber,
domain  tcdate           iOrderDate,
domain  tcdate           iLoadDate,
domain  tccom.bpid       iBuyFromBusinessPartner,
domain  tccom.bpid       iShipFromBusinessPartner,
domain  tcsite           iSite,
domain  tccwar           iWarehouse,
domain  tccwoc           iPurchaseOffice,
domain  tccfrw           iCarrier,
domain  tccom.cadr       iShipFromAddress,
domain  tccom.cadr       iReceiptAddress,
domain  tcitem           iItem,
domain  tccrte           iRoute,
domain  tcmcs.serv       iFreightLevel,
domain  tccdec           iDeliveryTerms,
domain  tcptpa           iPointOfTitlePassage,
ref     domain  tcdate           oPlannedReceiptDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function calculates the planned receipt date.
If the planned load date is filled, then the function uses the
planned load date and the transportation time to calculate the
planned receipt date.
In case no planned load date is available then the order date
will be used, and the Item Supplier lead times will be used to
calculate the planned receipt date.
The calculated receipt date is shifted forward to the
availability of the warehouse address calendar (calculated date
must be a workable date in the warehouse calendar).
Pre:    Not Applicable
Post:   Not Applicable
Input:  iOrderNumber            Purchase Order (No longer used)
iOrderDate              Order Date (Mandatory)
iLoadDate               Planned Load Date
iBuyFromBusinessPartner Buy from Business Partner (Mandatory)
iShipFromBusinessPartner
Ship from Business Partner (Mandatory)
iSite                   Site
iWarehouse              Warehouse
iPurchaseOffice         Purchase Office (Mandatory)
iCarrier                Carrier
iShipFromAddress        Ship from address (Mandatory)
iReceiptAddress         Receipt address (Mandatory if iWarehouse
is empty)
iItem                   Item (Mandatory)
iRoute                  Route
iFreightLevel           Freight Level
iDeliveryTerms          Delivery Terms
iPointOfTitlePassage    Point of Title Passage
Output: oPlannedReceiptDate     Planned Receipt Date
Return: 0                       Planned Receipt Date is calculated successfully
<> 0                    An error occurred.
```
