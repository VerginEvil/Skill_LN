# JobShopRouting.ClearUseForPlanning

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for JobShopRouting
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 659-660

```baan
DLL:   tiextrouapi
This function is available from 2021.05 (KB2156270).
Syntax: long JobShopRouting.ClearUseForPlanning(
domain  tcsite           iSite,
domain  tcitem           iProduct,
domain  tirou.rouc       iJobShopRouting,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function sets the Use For Planning flag to false for a Job
Shop Routing.
Pre:    Retry point must be set.
Post:   Commit or abort the transaction.
Input:  iSite                   - Site (Mandatory).
iProduct                - Product (Mandatory).
iJobShopRouting         - Job Shop Routing (Mandatory).
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Use for Planning set to false.
<> 0                    - Otherwise.
```
