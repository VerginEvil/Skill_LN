# ProductionOrderReject.Scrap

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrderReject
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 808-809

```baan
DLL:   tiextsfcapi
This function is available from     2020.11 (KB2156939  ).
Syntax: long ProductionOrderReject.Scrap(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tcopno           iOperation,
domain  tiqep2           iQuantity,
ref     domain  tcibd.sern       iSerialArray() fixed,
domain  tcuef.effn       iEffectivityUnit,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this public interface to scrap a quantity of rejected end
item of an operation, as in session tisfc0211m000.
Pre:    Retry point must be set.
Post:   Commit or abort the transaction.
Input:  iSite                   Site (mandatory when the Site concept
is active).
iProductionOrder        Production Order (mandatory and must be
in iSite).
iOperation              Operation (mandatory).
iQuantity               Quantity (mandatory).
For serialized items, this double
argument must have an integer value.
iSerialArray            Array of Serial Numbers.
Pass a filled array (static
or dynamic) when the main item is
serialized and serial numbers are required;
the length of the array must equal i.Quantity.
Pass an empty array variable when the main
item is not serialized. E.g. pass
the variable dummy.serials, which is
defined as:
domain tcibd.sern dummy.serials(1)
iEffectivityUnit        Effectivity Unit (optional).
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Rejected quantity is scrapped
<> 0                    Rejected quantity could not be scrapped
```

## Public Interfaces for WorkCenter

The following functions are available: WorkCenter.GetCalendar WorkCenters.StartOverview
