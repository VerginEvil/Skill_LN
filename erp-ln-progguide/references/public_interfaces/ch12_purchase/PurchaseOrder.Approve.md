# PurchaseOrder.Approve

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 441-442

```baan
DLL:   tdextpurapi
This function is available from     2026.07 (KB3682350  ).
Syntax: long PurchaseOrder.Approve(
domain  tcorno           iPurchaseOrder,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This Public Interface approves the given purchase order.
After the approval, the automatic order processing is executed.
This function contains its own transaction logic. As this Public
Interface starts Automatic Order Processing (which could take a
relatively long time) it is advised to not call this Public
Interface in a BOD or BDE context. Doing that would suppress
the internal transaction logic and would create one large database
transaction, with potential locking problems as a consequence.
Pre:    Not Applicable
Post:   Not Applicable
Input:  iPurchaseOrder                        - Purchase order (Mandatory)
iProcessingOptionSet                          - Processing Option Set (Optional).
If 0, the default approval options
are applied.
A Processing Option Set can be created
via a call to ProcessingOptionSet.Create()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete()
Processing Options have a direct relationship with the form fields
on session Approve Purchase Orders (tdpur4210m100). They are not
explained in further detail here.
Please refer to the session help for additional information.
Processing Options that are set while a required Implemented Software
Component is not available are ignored.
Supported Processing Options and their defaults:
NAME                                    TYPE                    DEFAULT
------------------------------------------------------------------------
RecalculatePriceDiscounts               domain tcgen.ynds       tcgen.ynds.no
RecalculateAttributeSurcharges          domain tcgen.ynds       tcgen.ynds.no
RedetermineMaterialPriceInfo            domain tcgen.ynds       tcgen.ynds.no
RecalculateLandedCosts                  domain tcgen.ynds       tcgen.ynds.no
OverwriteManualAndModifiedLandedCosts   boolean                 false
ApplyApprovalRules                      boolean                 false
CheckAmountUpto                         domain tcamnt           0.0
CheckAmountUptoCurrency                 domain tcccur           ""
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Approval was successful
<> 0                                          - An error occurred
```
