# SalesOrderLine.Split

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 358-359

```baan
DLL:   tdextslsapi
This function is available from 2025.07 (KB3567247).
Syntax: long SalesOrderLine.Split(
domain  tcorno           iSalesOrder,
domain  tcpono           iSalesOrderLine,
domain  tcpono           iSalesOrderLineSequence,
domain  tcqsl1           iQuantityForNewDetail,
domain  tcdate           iPlannedDeliveryDateForNewDetail,
domain  tcsite           iSiteForNewDetail,
domain  tccwar           iWarehouseForNewDetail,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function performs similar functionality as splitting sales order
lines/detail lines in the session "Sales Order Planned Delivery Lines"
(tdsls4101m100). It handles the splitting of a sales order line (option
"Generate Line" in session) and detail line (option "Split Line" in
session).
Note:
1. In case change requests are applicable and required, a CR is
initiated to perform the split action. An option is provided
to automatically approve/process the change request to the
order (it performs a straightforward approve; no recalculations
etc.). The change request will have origin 'Manual'.
2. This function does not trigger any automatic processing
afterwards, if applicable.
Pre:    Caller must set retry-point
Post:   Caller must commit/abort transaction
Input:  iSalesOrder             - Sales order (mandatory)
iSalesOrderLine         - Sales order line (mandatory)
iSalesOrderLineSequence - Sales order line sequence
iQuantityForNewDetail   - The quantity that will be used for the
new detail line (mandatory)
iPlannedDeliveryDateForNewDetail-
The planned delivery date that will be
used for the new detail line (mandatory)
iSiteForNewDetail       - The site that will be used for the new detail
line (mandatory if Sites is implemented)
iWarehouseForNewDetail  - The warehouse that will be used for the new
detail line (mandatory)
iProcessingOptionSet    - Processing Option Set (Optional).
If 0, the default options are applied.
A Processing Option Set can be created
via a call to ProcessingOptionSet.Create()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete()
Any options which are not available as Processing Option will get defaulted.
Processing Options which are set while a required Implemented Software Component
is not available are ignored.
Supported Processing Options and their defaults:
NAME                                            TYPE            DEFAULT
DeleteFreightOrder                              domain tcyesno  tcyesno.yes
Yes: If Freight Management is implemented
an existing freight order linked to
the sales order line will be deleted.
No:  If Freight Management is implemented
an existing freight order linked to
the sales order line will not be
deleted; by that the sales order line
will not be split.
ApproveAndProcessChangeRequestAutomatically     domain tcyesno  tcyesno.yes
Yes: If Change Requests are applicable,
the created change request will be
approved and processed automatically.
No:  Approval and processing of the
change request (if any) is not done
automatically.
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - The sales order line has been split.
<> 0                    - An error occurred
```
