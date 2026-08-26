# BRA.WarehouseReceipt.RevertBrazilianInvoice

> Chapter: Chapter 46 Public Interfaces for Localizations
>
> Group: Public Interfaces for BRA.WarehouseReceipt
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1917-1918

```baan
DLL:   lpextbraapi
This function is available from     2025.10 (KB3630696  ).
Syntax: long BRA.WarehouseReceipt.RevertBrazilianInvoice(
domain  tcncmp           iWarehouseCompany,
domain  whinh.shpm       iWarehouseReceiptId,
ref             long             oInvoiceLinesReverted,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function processes the reversal of warehouse receipt
lines from Brazilian invoice lines.
During this process, the transaction handling is being done in
this function, therefore, retry point, commit transaction and
abort transaction will be handled.
Pre:    No open database transaction.
Post:   n.a.
Input:  iWarehouseCompany                     - Warehouse company
iWarehouseReceiptId                           - Warehouse receipt ID
Output: oInvoiceLinesReverted                 - Number of Brazilian invoice lines
reverted.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0/DALHOOKERROR
```

## Public Interfaces for BRA.Department

The following functions are available: BRA.Department.GetEstablishmentCode
