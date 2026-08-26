# ProductionOrderOperation.GetMaximumQuantityToReportComplete

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrderOperation
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 792-793

```baan
DLL:   tiextsfcapi
This function is available from     2025.06 (KB3537727  ).
Syntax: long ProductionOrderOperation.GetMaximumQuantityToReportComplete(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tcopno           iOperation,
boolean          iIncludeCurrentOperation,
ref     domain  tiqep2           oMaximumQuantityToReport,
ref     domain  tcopno           oMostRestrictiveOperation,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface determines the highest quantity allowed to
be reported for the specified operation, determined by the
limitations set by previous operations for production order.
Pre:    N.A.
Post:   N.A.
Input:  iSite                   Site (Mandatory when the Site concept
is active).
iProductionOrder        Production Order (Mandatory. Must be in
iSite).
iOperation              Operation (Mandatory).
iIncludeCurrentOperation
Determines whether the current operation
is included when the maximum quantity to
report is calculated.
Output: oMaximumQuantityToReport
The maximum quantity to report for
the specified operation.
oMostRestrictiveOperation
The operation that dictates the
maximum quantity to report.
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Successfully determined maximum
quantity to be reported.
<> 0                    An error occurred in determining the
maximum quantity to be reported.
```
