# FreightPlanning.MoveShipmentToLoad

> Chapter: Chapter 26 Public Interfaces for Freight
>
> Group: Public Interfaces for FreightPlanning
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1322-1323

```baan
DLL:   fmextlbdapi
This function is available from     2019.08 (KB2070843  ).
Syntax: long FreightPlanning.MoveShipmentToLoad(
domain  tcorno           iShipment,
domain  tcorno           iDestinationLoad,
boolean          iAllowMergeShipmentLines,
boolean          iDeleteEmptyLoad,
boolean          iCalculateFreightCostsIfInteractive,
boolean          iCalculateAdditionalCosts,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface will move a Shipment to a Load.
Pre:    db.retry.point is set
Post:   transaction handling (abort/commit)
exception handling can be done when applicable
Input:  iShipment                             - Shipment which must be moved:
Mandatory
iDestinationLoad                              - Load to which the shipment must be
moved: Mandatory
iAllowMergeShipmentLines                      - When iDestinationLoad already has a
shipment line which has the same
freight order line of any of the
iSourceShipment lines, the lines must
be merged. This flag determines if
that should be allowed (true/false)
iDeleteEmptyLoad                              - If the load from which the
iSourceShipment is moved becomes empty
then it will be possible to remove
the empty load with the setting of
this flag.
iCalculateFreightCostsIfInteractive
-                                               If freight costs calculation is setup
to be recalculated interactively in
the parameters, in the standard a
question will be raised, with this
flag the calculation in such cases can
be set to true or false.
iCalculateAdditionalCosts
-                                               If freight costs are to be calculated
should the additional costs also be
calculated, true or false.
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

## Public Interfaces for Load

The following functions are available: Load.ConfirmDelivery
