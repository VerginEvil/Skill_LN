# Inventory.DetermineQuantity

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Inventory
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 939-941

```baan
DLL:   whextinaapi
This function is available from     2021.08 (KB2192478  ).
Syntax: long Inventory.DetermineQuantity(
domain  tcitem           iItem,
domain  tccwar           iWarehouse,
domain  tcowns           iOwnership,
boolean          iSpecificOwnerBuyFromBusinessPartner,
domain  tccom.bpid       iOwner,
domain  tccom.bpid       iBuyFromBusinessPartner,
boolean          iSpecificProject,
domain  tccprj           iProject,
boolean          iSpecificLot,
domain  tcclot           iLot,
boolean          iSpecificSerial,
domain  tcibd.sern       iSerial,
boolean          iQuarantineInventory,
domain  tcdate           iValuationDate,
boolean          iIncludeAntedated,
ref     domain  tcqiv1           oInventory,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface will determine the inventory quantity
at a certain date.
Pre:    N.A.
Post:   N.A.
Input:  iItem
The item for which inventory quantity needs
to be determined. This is mandatory to fill.
iWarehouse
The warehouse for which inventory quantity
needs to be determined. This is mandatory to fill.
iOwnership
The ownership for which inventory quantity needs
to be determined. This is mandatory to fill.
Possible options:
* Company Owned (tcowns.comp.owned)
* Consigned (tcowns.consigned)
* Customer Owned (tcowns.cust.owned)
iSpecificOwnerBuyFromBusinessPartner
Indicator (True/False) if inventory quantity needs to
be determined for a specific Owner and Buy from
Business Partner.
This indicator can only be set to True when iOwnership
is Consigned or Customer Owned.
This is mandatory to fill.
iOwner
The owner for which inventory quantity needs to be
determined.
This is mandatory to fill when
iSpecificOWnerBuyFromBusinessPartner is set to True
iBuyFromBusinessPartner
The buy                              -from business partner for which inventory
quantity needs to be determined.
This is mandatory to fill when
iSpecificOWnerBuyFromBusinessPartner is set to True and
iOwnership is Consigned.
iSpecificProject
Indicator (True/False) if inventory quantity needs to be
determined for a specific project.
This is mandatory to fill.
iProject
The project for which inventory quantity
needs to be determined.
This is optional to fill.
When iSpecificProject is set to False then all inventory
will be taken into account regardless of project.
When iSpecificProject is set to True and iProject is
filled then the inventory of the specified project will
be taken into account.
When iSpecificProject is set to True and iProject is not
filled then all not project related inventory will be
taken into account.
iSpecificLot
Indicator (True/False) if inventory quantity needs to be
determined for a specific lot.
This indicator can only be set when:
-                                iOwnership is Company Owned and
-                                item is defined as lot controlled in inventory and
-                                iSpecificProject = False
This is mandatory to fill.
iLot
The lot for which inventory quantity needs to be
determined. This is mandatory to fill if iSpecificLot
is set to True.
iSpecificSerial
Indicator (True/False) if inventory quantity needs to
be determined for a specific serial. This indicator can
only be set when:
-                                iOwnership is Company Owned and
-                                item is defined as serialized in inventory and
-                                iSpecificProject = False
This is mandatory to fill.
iSerial
The serial for which inventory quantity needs to be
determined. This is mandatory to fill if iSpecificSerial
is set to True.
iQuarantineInventory
Indicator if the inventory quantity needs to
be determined for quarantine inventory.
This is mandatory to fill.
iValuationDate
The date for which inventory quantity needs to be
determined. This is optional to fill.
When leaving empty the current date will be used.
iIncludeAntedated
Indicator (True/False) if antedated transactions should
be included or not.
Antedated transactions are transactions having
transaction date before the valuation date and actual
log date after the valuation date.
This is mandatory to fill.
Output: oInventory
The determined inventory quantity
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
