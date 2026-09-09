# ProductionOrder.FinishOperationAddition

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 713-713

```baan
DLL:   tiextsfcapi
This function is available from 2024.10 (KB3511148).
Syntax: long ProductionOrder.FinishOperationAddition(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   With this Public Interface, the production order that was
prepared for having operation(s) added
(via ProductionOrder.StartOperationAdditions), is reset to
standard behavior.
Input:  iSite                   Site (mandatory when the Site concept
is active).
iProductionOrder        Production Order (mandatory and must be
in iSite).
Output: oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Operation(s) added via Public Interface
ProductionOrder.StartOperationAdditions
has reset successfully.
<> 0                    Errors occurred.
```
