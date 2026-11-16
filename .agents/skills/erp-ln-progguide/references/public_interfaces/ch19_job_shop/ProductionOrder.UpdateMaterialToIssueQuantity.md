# ProductionOrder.UpdateMaterialToIssueQuantity

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 780-781

```baan
DLL:   tiextsfcapi
This function is available from 2023.02 (KB2244728).
Syntax: long ProductionOrder.UpdateMaterialToIssueQuantity(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
domain  tcpono           iMaterialPosition,
domain  tcqcp1           iQuantityToIssue,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Use this Public Interface to update the To Issue field for a
Production Order Material Position. The update can also affect
the value of the Subsequent Delivery field, following the logic
of session Material to Issue for Production Orders
(ticst0101m100).
Pre:    Retry point must be set.
Post:   Commit or abort the transaction.
Input:  iSite                   Site (mandatory when the Site concept
is active).
iProductionOrder        Production Order (mandatory, must be
in iSite).
iMaterialPosition       Material Position (Mandatory).
iQuantityToIssue        The quantity to set the To Issue field
to (Mandatory).
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       The To Issue field has been updated.
<> 0                    The To Issue field has not been updated.
```
