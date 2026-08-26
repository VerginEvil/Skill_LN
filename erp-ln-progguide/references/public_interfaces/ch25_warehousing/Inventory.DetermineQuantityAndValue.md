# Inventory.DetermineQuantityAndValue

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Inventory
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 941-943

```baan
DLL:   whextinaapi
This function is available from     2021.03 (KB2175297  ).
Syntax: long Inventory.DetermineQuantityAndValue(
domain  tcitem           iItem,
domain  tccwar           iWarehouse,
domain  tcowns           iOwnership,
domain  tccom.bpid       iOwner,
domain  tccom.bpid       iBuyFromBusinessPartner,
domain  tcyesno          iSpecificProject,
domain  tccprj           iProject,
domain  tcyesno          iQuarantineInventory,
domain  tcdate           iValuationDate,
domain  tcccur           iCurrency,
domain  tcrtyp           iRateType,
ref     domain  tcqiv1           oInventory,
ref             long             oNumberOfCostComponents,
ref     domain  tccpcp           oCostComponents() fixed,
ref     domain  tcphrs           oInventoryHours(),
ref     domain  tcamnt           oInventoryValue(),
ref     domain  tcphrs           oInventoryTotalHours,
ref     domain  tcamnt           oInventoryTotalValue,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface will determine the inventory and the
inventory value based on the valuation method on a certain date.
Note: This Public Interface does not include antedated
transactions and is replaced by a new version. Use
Inventory.DetermineQuantityAndValueV2 which has:
1) the option to define whether antedated transactions
should be included yes or no.
2) the option to detemine inventory quantity and value by
specific lot (lot pricing) or serial (serial pricing).
Pre:    N.a.
Post:   oCostComponents, oInventoryHours and oInventoryValue will be
allocated, so a free.mem() must be used to free the memory which
is used by these arrays.
Input:  iItem
The item for which inventory and inventory value needs
to be determined. This is mandatory to fill.
iWarehouse
The warehouse for which inventory and inventory value
needs to be determined. This is mandatory to fill.
iOwnership
The ownership for which inventory and inventory value
needs to be determined. This is mandatory to fill.
Possible options:
* Company Owned (tcowns.comp.owned)
* Consigned (tcowns.consigned)
* Customer Owned (tcowns.cust.owned)
iOwner
The owner for which inventory and inventory value needs
to be determined. This is mandatory to fill when
iOwnership is Consigned or Customer Owned
iBuyFromBusinessPartner
The buy                              -from business partner for which inventory and
inventory value needs to be determined. This is
mandatory to fill when iOwnership is Consigned.
iSpecificProject
Indicator if inventory and inventory value needs to be
determined for a specific project. This is mandatory to
fill.
iProject
The project for which inventory and inventory value
needs to be determined. This is optional to fill.
When iSpecificProject is set to No then all inventory
will be taken into account.
When iSpecificProject is set to yes and iProject is
filled then the inventory of the specified project will
be taken into account.
When iSpecificProject is set to yes and iProject is not
filled then all not project related inventory will be
taken into account.
iQuarantineInventory
Indicator if the inventory and inventory value needs to
be determined for quarantine inventory.
This is mandatory to fill.
iValuationDate
The date for which inventory and inventory value
needs to be determined. This is optional to fill.
When leaving it empty the current date will be used.
iCurrency
The currency in which the inventory value needs to be
expressed. This is mandatory to fill.
iRateType
The rate type for which inventory and inventory value
needs to be determined. This is optional to fill.
If empty the internal rate type is used.
Output: oInventory
The determined inventory.
oNumberOfCostComponents
The number of cost components.
oCostComponents
Array with the found cost components.
oInventoryHours
Array with the found inventory hours.
oInventoryValue,
Array with the found inventory values.
oInventoryTotalHours
The total inventory hours.
oInventoryTotalValue,
The total inventory value.
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0               - The inventory and inventory value have been found
successfully.
<> 0                       - Error. The inventory and inventory value could not be
determined.
```
