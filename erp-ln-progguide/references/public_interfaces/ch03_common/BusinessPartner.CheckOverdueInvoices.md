# BusinessPartner.CheckOverdueInvoices

> Chapter: Chapter 3 Public Interfaces for Common
>
> Group: Public Interfaces for BusinessPartner
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 117-118

```baan
DLL:   tcextcomapi
This function is available from     2020.08 (KB2122836  ).
Syntax: long BusinessPartner.CheckOverdueInvoices(
domain  tcncmp           iFinancialCompany,
domain  tccom.bpid       iInvoiceToBusinessPartner,
domain  tccwoc           iDepartment,
domain  tcyesno          iIncludeAnticipatedReceipts,
domain  tcdate           iDueDate,
ref     domain  tcyesno          oOverdueAmountExceedsTolerance,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.   :
This function checks if the business partner has overdue
invoices. If so, this function will compare the total overdue
amount with the tolerance amount(tccom112.tamd) or percentage
of the credit limit (tccom112.tpcd).
If the overdue amount is above the tolerance,
then o.overdue.amout.exceeds.tolerance becomes tcyesno.yes
When both fields (tccom112.tamd and tccom112.tpcd) are 0, then it
has to give the signal every time the due amount is greater than 0.
If the user wants to avoid the signal, the percentage has to be filled
with 100% and then the full credit limit will be used.
This of course requires that the credit limit has been set.
Pre     : NA
Post    : NA
Input   : iFinancialCompany                   - financial company number (mandatory)
iInvoiceToBusinessPartner
-                                               invoice-to business partner (mandatory)
iDepartment                                   - department (optional)
iIncludeAnticipatedReceipts
-                                               anticipated receipts yes/no (mandatory)
iDueDate                                      - date till which overdue invoices
are calculated (mandatory)
Output  : oOverdueAmountExceedsTolerance
-                                                'Yes' when total overdue amout
exceeds tolerance else 'No'.
oExceptionMessage                             - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Total overdue amount determined.
<> 0                                          - Error occurred.
```
