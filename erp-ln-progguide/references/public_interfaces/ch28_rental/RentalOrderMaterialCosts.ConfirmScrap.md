# RentalOrderMaterialCosts.ConfirmScrap

> Chapter: Chapter 28 Public Interfaces for Rental
>
> Group: Public Interfaces for RentalOrderMaterialCosts
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1587-1589

```baan
DLL:   tsextsocapi
This function is available from     2026.09 (KB3691643  ).
Syntax: long RentalOrderMaterialCosts.ConfirmScrap(
domain  tcorno           iRentalOrder,
domain  tcpono           iMaterialLine,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this function to Confirm Scrap for a Rental Order
Material Line. The Material Line can belong to an Agreement,
as well as a Maintenance Activity.
Pre:    Set db.retry.point
Post:   Abort/Commit Transaction
Input:  iRentalOrder
Rental Order
Mandatory.
iMaterialLine
Rental Order Material Line
Not Mandatory.
If not specified, Confirm Scrap is done for Material
Lines of the Rental Order with delivery type "To Scrap".
iProcessingOptionSet
Processing Option Set: a processing option set number
referring to a processing option set containing at
least one valid option.
Not Mandatory.
NAME                    TYPE                    DEFAULT
================================================================
ContinueWhenSerialNumberNotFilledForSerializedControlledItem
domain  tcyesno         tcyesno.no
If this option is no, then confirming scrap is not allowed
when the item is serialized controlled, but no serial number is
filled.
Output: oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0                     - No Error
<> 0                          - Error
```

## Chapter 29 Public Interfaces for Invoicing

## Public Interfaces for Invoice

The following functions are available: Invoice.ComposePrintPostInvoices Invoice.CreditInvoiceLine Invoice.GetInterimRevenueLedgerAccountAndDimensions Invoice.Reprint Invoice.StartInvoicing360 Invoice.StartMultiMain
