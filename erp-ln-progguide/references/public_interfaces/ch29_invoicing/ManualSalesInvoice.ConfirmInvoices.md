# ManualSalesInvoice.ConfirmInvoices

> Chapter: Chapter 29 Public Interfaces for Invoicing
>
> Group: Public Interfaces for ManualSalesInvoice
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1611-1613

```baan
DLL:   ciextsliapi
This function is available from     2025.05 (KB3553572  ).
Syntax: long ManualSalesInvoice.ConfirmInvoices(
domain  tcncmp           iFinancialCompany,
boolean          iContinueIfShipToBusinessPartnerIsInactive,
domain  tcorno           iManualSalesInvoiceFrom,
domain  tcorno           iManualSalesInvoiceTo,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface is used to confirm the manual sales
invoices for the given range of manual sales invoice Id's.
The lines whose status is On                      -hold will be set to confirmed.
Note:                       - Transaction handling is done within the function. The
commit will be done per manual sales id.
The behaviour is set similar to cisli2219m000 session.
Pre:    Not applicable.
Post:   Not applicable.
Input:  iContinueIfShipToBusinessPartnerIsInactive
-                                       This variable is taken into account only when
Ship                                        -to Business Partner of the Manual Sales
invoice is Inactive.
-                                       Possible values are:
True:                                       - If Ship-to business partner status is
not active then manual sales invoice
will be confirmed but Ship                                              -to Business
Partner will be empty in the billable
lines.
False:                                      - If Ship-to business partner status is
not active then the manual sales invoice
will not be confirmed and the process
will skip the record and search for the
next record.
iFinancialCompany                             - Financial Company
(This is a Mandatory field)
iManualSalesInvoiceFrom                       - Manual Sales Invoice From
(This is a Mandatory field)
iManualSalesInvoiceTo                         - Manual Sales Invoice To
(This is a Mandatory field)
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Manual Sales Invoices confirmed
successfully
<> 0                                          - Otherwise
```

## Chapter 30 Public Interfaces for Taxation

## Public Interfaces for Tax

The following functions are available: Tax.AddAdjustment Tax.Calculate Tax.CalculateTaxBaseAmount Tax.GetBusinessPartnerTaxRegistrationID Tax.GetDefaultsGoods Tax.GetExternalTaxDetails Tax.GetInternalTaxDetails Tax.GetRate Tax.ProcessTestScenario
