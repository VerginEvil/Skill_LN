# ProductionOrder.NewVersion

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 721-721

```baan
DLL:   tiextsfcapi
This function is available from     2023.03 (KB2274584  ).
Syntax: long ProductionOrder.NewVersion(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this Public Interface to update the status of the given
Production Order to Modify. The update also increases the
version number of the Production Order, following the logic
of session Production Order (tisfc0101m100).
Pre:    Retry point must be set.
Post:   Commit or abort the transaction.
Input:  iSite                   Site (mandatory when the Site concept
is active).
iProductionOrder        Production Order (mandatory, must be
in iSite).
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       The status has been updated.
<> 0                    The status has not been updated.
```
