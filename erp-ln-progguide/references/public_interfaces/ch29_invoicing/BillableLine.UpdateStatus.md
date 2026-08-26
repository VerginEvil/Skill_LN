# BillableLine.UpdateStatus

> Chapter: Chapter 29 Public Interfaces for Invoicing
>
> Group: Public Interfaces for BillableLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1610-1611

```baan
DLL:   ciextsliapi
This function is available from     2024.09 (KB3519213  ).
Syntax: long BillableLine.UpdateStatus(
domain  tcncmp           iSourceCompany,
domain  tcsli.srtp       iSourceType,
domain  tcorno           iOrderNumber,
domain  tcsli.orln       iOrderLine,
domain  tcsli.oref       iOrderReference,
domain  tcsli.tref       iTechnicalReference,
domain  tcpono           iBillingSequence,
domain  tcsli.stat       iNewBillableLineStatus,
boolean          iSynchronizeBillingSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface is used to update the billable line
status to the given new status if possible.
Pre:    Caller must set retry              -point.
Post:   Caller must commit/abort transaction.
Input:  i.calling.api                         - Calling API
iSourceCompany                                - Source Company
(This is a Mandatory field)
iSourceType                                   - Source Type
(This is a Mandatory field)
iOrderNumber                                  - Order Number
(This is a Mandatory field)
iOrderLine                                    - Order Line
iOrderReference                               - Order Reference
iTechnicalReference                           - Technical Reference
iBillingSequence                              - Billing Sequence
(This is a Mandatory field)
iNewBillableLineStatus                        - New Billable Line Status
(This is a Mandatory field)
iSynchronizeBillingSet                        - Synchronize the status for all the
billable lines having the same billing
set.
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Billable Line updated successfully
<> 0                                          - Otherwise
```

## Public Interfaces for ManualSalesInvoice

The following functions are available: ManualSalesInvoice.ConfirmInvoices
