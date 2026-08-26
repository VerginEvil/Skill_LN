# ServiceOrderActivity.StartMultiMain

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for ServiceOrderActivity
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1452-1453

```baan
DLL:   tsextsocapi
This function is available from     2022.10 (KB2262990  ).
Syntax: long ServiceOrderActivity.StartMultiMain(
long             iStartMode,
domain  tcmcs.st30       iStartFilter,
const           string           iQueryExtend(),
domain  tcorno           iServiceOrder,
domain  tsmdm.acln       iActivityLine,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts the Multi Main Table session Service Order
Activity (tssoc2110m100).
Input:  iStartMode
Specifies the start mode for the session.
Possible values are:
MODAL                               -         The parent session is blocked until the
child session exits. The session will be
started as a zoom session.
MODELESS                               -      Parent and child are parallel
sessions that can be manipulated
simultaneously.
iStartFilter            Not Used.
iQueryExtend            A specific query to be used when zooming
to this session.
iServiceOrder           Service Order
iActivityLine           Service Order Activity line number
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Session started
<> 0                    An error occurred
```

## Public Interfaces for ServiceOrderMaterialCosts

The following functions are available: ServiceOrderMaterialCosts.ConfirmScrap ServiceOrderMaterialCosts.ProcessReturnDeliveries ServiceOrderMaterialCosts.RecalculatePriceDiscounts
