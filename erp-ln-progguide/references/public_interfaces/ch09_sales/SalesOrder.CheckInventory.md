# SalesOrder.CheckInventory

> Chapter: Chapter 9 Public Interfaces for Sales
>
> Group: Public Interfaces for SalesOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 315-316

```baan
DLL:   tdextslsapi
This function is available from     2026.07 (KB3682826  ).
Syntax: long SalesOrder.CheckInventory(
domain  tcorno           iSalesOrder,
long             iProcessingOptionSet,
ref             boolean          oLineProcessed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function handles the inventory check for the given sales
order.
Transaction handling:
Retry                         -point and commit/abort transaction is handled within
this function.
Pre:                  -
Post:                 -
Input:  iSalesOrder                           - Sales Order (Mandatory)
iProcessingOptionSet                          - Optional. If 0, the default options
are applied.
A Processing Option Set can be created via a
call to ProcessingOptionSet.Create() in
DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete()
Processing Options have a direct relationship with the form fields
on session "Check Inventory Sales Orders" (tdsls4217m000)
and are not explained in further detail here. Please refer to the
session help for additional information.
Check              -Inventory options which are not available as Processing Options
will get defaulted in accordance with the defaults shown below.
Processing Options which are set while a required Implemented
Software Component is not available are ignored.
NAME                                    TYPE                    DEFAULT
SortLinesBy                             domain tdsls.slbd       tdsls.slbd.odat
Output: oLineProcessed                        - True:  At least one record has been
processed successfully
False: no record has been processed
successfully
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Check Inventory was successful, or
no checking needed to be done.
<> 0                                          - An error occurred
```
