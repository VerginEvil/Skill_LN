# SalesOrder.CreditCheck

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 317-318

```baan
DLL:   tdextslsapi
This function is available from     2025.05 (KB3565482  ).
Syntax: long SalesOrder.CreditCheck(
domain  tcorno           iSalesOrder,
long             iPhaseNumber,
domain  tcyesno          iBlock,
ref             boolean          oBlocked,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function checks if a sales order (or an open sales order change
request) must be blocked based on the credit check logic. If so, the
sales order will be blocked in case input argument "iBlock" is 'Yes'.
Credit control is done based on the phase number, input argument
"iPhaseNumber", in which it has to take place. Phase 1 represents the
'Order Entry' moment, phase 2 represents the 'Release to Warehousing'
moment and phase 3 represents the 'Confirm Shipment' moment; independent
of how far a sales order line really is in the process.
Signalling and/or blocking depends on the setup.
When concept "Change Request" is implemented and for the given sales
order an open sales order change request exists, that change request
should be used as input argument for "iSalesOrder".
Pre:    Caller must set retry              -point
Post:   Caller must commit/abort transaction
Input:  iSalesOrder                           - Sales Order (mandatory)
iPhaseNumber                                  - Phase Number to check
1 = 1st phase credit check (order entry)
2 = 2nd phase credit check (release to
warehouse)
3 = 3rd phase credit check (confirm shipment)
iBlock                                        - Indicates if the sales order should be blocked
or only a message should be given (based
on sales parameters and/or settings).
Output: oBlocked                              - True: Sales order is (already) blocked
-                                               False: Sales order is not blocked
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - No error
<> 0                                          - Error occurred
```
