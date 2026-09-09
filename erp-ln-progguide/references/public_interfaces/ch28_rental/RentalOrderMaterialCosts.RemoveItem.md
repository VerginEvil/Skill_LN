# RentalOrderMaterialCosts.RemoveItem

> Chapter: Chapter 28 Public Interfaces for Rental
>
> Group: Public Interfaces for RentalOrderMaterialCosts
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1603-1604

```baan
DLL:   tsextsocapi
This function is available from 2026.10 (KB3699767).
Syntax: long RentalOrderMaterialCosts.RemoveItem(
domain  tcorno           iRentalOrder,
domain  tcpono           iMaterialLine,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function removes a serialized or non-serialized item
for a rental order material line.
When the item is serialized, the serialized item status is
changed to 'Removed'.
If ReplacementForLineExists is not specified as 'true', then
the serialized or non-serialized item is also removed from the
physical breakdown.
If the item is serialized and the material line is company
owned, then the Sold-to BP is emptied in the serialized item.
If additionally the serialized item is externally owned and in
an active installation, the installation is expired and the
installation group is emptied in the serialized item. Next to
that, the top item and serial number are updated for the
serialized item on the material line and all its children in
the physical breakdown; the serialized item on the material line
becomes the new top serialized item.
Pre:    Set db.retry.point
Post:   Abort/Commit Transaction
Input:  iRentalOrder
Rental Order
Mandatory.
iMaterialLine
Material Line
Mandatory.
iProcessingOptionSet
Processing Option Set: a processing option set number
referring to a processing option set containing at
least one valid option.
Not Mandatory.
NAME                    TYPE                    DEFAULT
================================================================
ReplacementForLineExists
boolean                 false
If this option is 'false', then the serialized or non-serialized
item will be removed from the physical breakdown. This is done
via a Physical Breakdown Change which is linked to the order.
Output: oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0       - No Error
<> 0    - Error
```
