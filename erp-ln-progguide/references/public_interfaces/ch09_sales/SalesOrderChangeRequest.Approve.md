# SalesOrderChangeRequest.Approve

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrderChangeRequest
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 369-370

```baan
DLL:   tdextslsapi
This function is available from 2023.06 (KB2290338).
Syntax: long SalesOrderChangeRequest.Approve(
domain  tcorno           iChangeRequest,
domain  tcgen.ynds       iRecalculatePriceAndDiscounts,
domain  tcgen.ynds       iRedetermineMaterialPrice,
domain  tcgen.ynds       iRecalculateAdditionalCosts,
ref             boolean          oChangeRequestApproved,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function approves a modified sales order change request.
Pre:    LN Application sets retry-point, so not by caller
Post:   LN Application sets commit/abort transaction, so not by caller
Input:  iChangeRequest                  - Sales Order Change Request (mandatory)
iRecalculatePriceAndDiscounts   - Recalculate Price and Discounts
(mandatory)
iRedetermineMaterialPrice       - Redetermine Material Price (mandatory)
iRecalculateAdditionalCosts     - Recalculate Additional Costs (mandatory)
Output: oChangeRequestApproved          - Approved Sales Order Change Request
(true/false)
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0       -> No error
<> 0    -> Error occurred
```
