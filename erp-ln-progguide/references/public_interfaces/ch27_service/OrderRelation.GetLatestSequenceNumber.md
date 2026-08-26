# OrderRelation.GetLatestSequenceNumber

> Chapter: Chapter 27 Public Interfaces for Service
>
> Group: Public Interfaces for OrderRelation
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1538-1540

```baan
DLL:   tsextmdmapi
This function is available from     2026.09 (KB3689060  ).
Syntax: long OrderRelation.GetLatestSequenceNumber(
domain  tckoor           iOrderOrigin,
domain  tcorno           iOrder,
domain  tcpono           iOrderLine,
domain  tcpono           iDetailLine,
domain  tckotr           iTransactionType,
ref     domain  tcpono           oSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  This function fetches from entity Service - Order Relations
(tsmdm400) the latest Sequence Number (tsmdm400.rseq) for
Related Order Type 'Warehousing Order'.
This Sequence Number is necessary when calling Public Interface
ProductAvailability.GetDeliveryDate.
When there is no related order yet, the returned Sequence is
set to 1.
Pre:                  -
Post:                 -
Input:
iOrderOrigin
Origin / Order Type
Mandatory.
Supported Origins are:
tckoor.act.srv
tckoor.act.srv.man
tckoor.act.srv.sls
tckoor.act.srv.sls.man
tckoor.act.dpt.wrk
tckoor.act.dpt.wrk.man
tckoor.customer.claim
tckoor.supplier.claim
iOrder
Order/Claim number
Mandatory.
iOrderLine
Order line / Activity
Not mandatory.
iDetailLine
Detail Line, like Service Order Material Line
Not mandatory.
iTransactionType
Transaction Type (Issue/Receipt)
Mandatory.
Output:
oSequence
Latest Sequence Number
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0       No errors occurred.
<> 0    Error(s) occurred.
```

## Chapter 28 Public Interfaces for Rental

## Public Interfaces for RentalOrder

The following functions are available: RentalOrder.Cancel RentalOrder.Close RentalOrder.Complete RentalOrder.Cost RentalOrder.Generate RentalOrder.Plan RentalOrder.Release RentalOrder.StartMultiMain
