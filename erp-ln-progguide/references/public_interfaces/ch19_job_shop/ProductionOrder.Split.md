# ProductionOrder.Split

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 771-772

```baan
DLL:   tiextsfcapi
This function is available from     2024.11 (KB3512062  ).
Syntax: long ProductionOrder.Split(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tiqep3           iSplitQuantity,
domain  tccdis           iReasonCode,
ref     domain  tcibd.sern       iSelectedSerialNumbers() fixed,
long             iNumberOfSelectedUnits,
ref     domain  tcuef.effn       iSelectedUnitNumbers(),
ref     domain  tiqep3           iSelectedUnitQuantity(),
ref     domain  tcpdno           oCreatedProductionOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Function is used to split off a part of the to be produced
quantity of a selected production order. Production Order
documents will not be printed, but should be printed by using
the available print functions.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iSite                   Site (Mandatory when the Site concept
is active).
iProductionOrder        Production Order (Mandatory).
iSplitQuantity          Quantity to be split off from the
Production Order.
iReasonCode             Reason Code for splitting off a
quantity (Mandatory based on Production
Settings).
iSelectedSerialNumbers  Selected Serial Numbers is an array
whose length equals the split quantity
(Mandatory if the Item is serialized).
iNumberOfSelectedUnits  Number of Selected Units.
iSelectedUnitNumbers    Selected Unit Numbers is an array whose
length equals the Number of Selected
Units.
iSelectedUnitQuantity   Selected Unit Quantity is an array whose
length equals the Number of Selected
Units.
Output: oCreatedProductionOrder Production Order created after
splitting.
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Production Order split is successful.
<> 0                    Errors occurred.
```
