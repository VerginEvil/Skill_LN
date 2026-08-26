# Inventory.Start360

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for Inventory
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 950-951

```baan
DLL:   whextwmdapi
This function is available from     2024.02 (KB2317999  ).
Syntax: long Inventory.Start360(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
long             iSessionIndex,
const           string           iQueryExtend(),
domain  tcyesno          iSetFilterFields,
domain  tcsite           iSite,
domain  tccwar           iWarehouse,
domain  tccitg           iItemGroup,
domain  tcitem           iItem,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the session Inventory 360 (whwmd4300m000).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits, the session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter
Specifies the start filter that is to be applied to the
started session.
Possible values are:
"":
iSessionIndex
Not Used.
iQueryExtend
A specific query to be used when zooming to this session.
iSetFilterFields:
Used to set a filter on the Inventory for a Warehouse or
an Item Group.
Possible values are:
Yes:    A filter on the inventory for a Warehouse or an
Item Group can be applied.
No:     No filter for Warehouse or Item Group will be
applied.
Empty:  If not set, the saved session defaults will be
used and applied for these filter fields.
iSite:
The Site to be used with iSetFilterFields.
iWarehouse:
The Warehouse to be used with iSetFilterFields.
iItem Group:
The Item Group to be used with iSetFilterFields.
iItem
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Session started
<> 0                                          - Error
```

## Public Interfaces for SpecificationInventory

The following functions are available: SpecificationInventory.GetUnallocatedAvailableQuantity
