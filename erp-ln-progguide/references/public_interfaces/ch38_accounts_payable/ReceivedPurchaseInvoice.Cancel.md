# ReceivedPurchaseInvoice.Cancel

> Chapter: Chapter 38 Public Interfaces for Accounts Payable
>
> Group: Public Interfaces for ReceivedPurchaseInvoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1798-1799

```baan
DLL:   tfextacpapi
This function is available from     2025.05 (KB3578856  ).
Syntax: long ReceivedPurchaseInvoice.Cancel(
domain  tcncmp           iReceivedInvoiceCompany,
domain  tfacp.rinv       iReceivedPurchaseInvoice fixed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface Cancels a Received Purchase Invoice
Pre:    set db.retry point()
Post:   set commit/abort.transaction()
Input:  iReceivedInvoiceCompany               - Received Invoice Company  - mandatory
iReceivedPurchaseInvoice                      - Received Purchase Invoice - mandatory
Output:
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Succes
<> 0                                          - Otherwise
```

## Public Interfaces for PurchaseInvoice

The following functions are available: PurchaseInvoice.StartMultiMain
