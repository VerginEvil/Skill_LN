# MaintenanceSalesOrder.Cost

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for MaintenanceSalesOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1472-1473

```baan
DLL:   tsextmscapi
This function is available from     2025.06 (KB3569267  ).
Syntax: long MaintenanceSalesOrder.Cost(
domain  tcorno           iMaintenanceSalesOrder,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function sets the Maintenance Sales Order, and all
related Part Lines and Coverage Lines, to Costed.
Pre:    db.retry.point must have been set.
Call ProcessingOptionSet.Create() to obtain
iProcessingOptionSet.
Post:   Commit/abort the transaction.
Delete the option set by calling ProcessingOptionSet.Delete().
Input:  iMaintenanceSalesOrder                - Maintenance Sales Order; mandatory
iProcessingOptionSet
Processing Option Set: a processing option set number
referring to a processing option set containing at
least one valid option.
Mandatory.
NAME                    TYPE                    DEFAULT
================================================================
InvoiceFreightLines
domain  tcyesno         yes
When there are Part Lines with related Freight Lines,
these Freight Lines are sent to Invoicing.
IgnoreUnapprovedPurchaseInvoices
domain  tcyesno         no
If this argument is set to Yes, the maintenance sales
order is costed, even when there are unapproved
purchase invoices present.
Output  :
ExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return  : 0                                   - No error; however, error messages can
have been set.
<> 0                                          - An error occurred
```
