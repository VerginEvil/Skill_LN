# ReceivedPurchaseInvoice.Validate

> Chapter: Chapter 38 Public Interfaces for Accounts Payable
>
> Group: Public Interfaces for ReceivedPurchaseInvoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1819-1819

```baan
DLL:   tfextacpapi
This function is available from 2026.10 (KB3680391).
Syntax: long ReceivedPurchaseInvoice.Validate(
domain  tcncmp           iReceivedInvoiceCompany,
domain  tfacp.rinv       iReceivedPurchaseInvoice fixed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface Validates a Received Purchase Invoice.
The validation reads missing data, validates the invoice data
(Business Partner, header, lines, tax lines) and sets the
status accordingly.
The result of the validation is reflected in the status of
the Received Purchase Invoice (tfacp110): either 'Validated'
or 'Validation Errors'.
Pre:    N.A.
Post:   Transaction management is handled internally.
Input:  iReceivedInvoiceCompany - Received Invoice Company  - mandatory
iReceivedPurchaseInvoice- Received Purchase Invoice - mandatory
Output:
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Success (validation done; result
could be 'validated' or
'validation errors')
<> 0                    - Otherwise (technical error)
```
