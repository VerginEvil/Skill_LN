# ProductionOrderOperation.SetRemainderStartDate

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrderOperation
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 801-802

```baan
DLL:   tiextsfcapi
This function is available from 2021.10 (KB2212649).
Syntax: long ProductionOrderOperation.SetRemainderStartDate(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tcopno           iOperation,
domain  tcutcs           iRemainderStartDate,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface will update the Remainder Start Date for
a Production Order Operation.
Pre:    Retry point must be set.
Post:   Commit or abort the transaction.
Input:  iSite                   Site (mandatory if active).
iProductionOrder        Production Order (mandatory).
iOperation              Production Order Operation (mandatory).
iRemainderStartDate     The Remainder Start Date for the
Production Order Operation (mandatory).
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Remainder Start Date has been updated.
<> 0                    - Remainder Start Date has not been
updated.
```
