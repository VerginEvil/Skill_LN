# PurchaseOrderLine.ReleaseToWarehousing

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 463-464

```baan
DLL:   tdextpurapi
This function is available from     2021.12 (KB2218711  ).
Syntax: long PurchaseOrderLine.ReleaseToWarehousing(
domain  tcorno           iPurchaseOrder,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderLineSequence,
ref     domain  tcyesno          oReleased,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function handles the release of a purchase order line to
warehousing.
If applicable, this function will execute the Price Stage
blocking functionality. As a result, the order line can be
blocked and no release is done. This is not an error situation
so the function returns with 0. Moreover, the caller must still
commit the transaction, otherwise the Price                      -Stage Blocking
changes are not committed to the database.
Pre:    Caller must set retry              -point
Post:   Caller must commit/abort transaction
Input:  iPurchaseOrder  Purchase Order (Mandatory)
iOrderLine              Purchase Order Line (Mandatory)
iOrderLineSequence      Purchase Order Line Sequence.
Output: oReleased               Yes: The order line has been released to
warehousing
No:  The order line has not been released
to warehousing. Error or
information messages may be present
in oExceptionID.
oExceptionMessage       The last message. This can also be filled
if the return value equals 0.
If more than one  message is given,
these are present in the oExceptionID
oExceptionID            An ID that refers to all error
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       The function has been executed
successfully. Either Release to Warehousing
has been executed, or the order line is
blocked due to Price Stages.
<> 0                    An error occurred
```
