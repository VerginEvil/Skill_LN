# ProductionOrder.ProcessReturn

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 748-749

```baan
DLL:   tiextsfcapi
This function is available from 2023.11 (KB2302401).
Syntax: long ProductionOrder.ProcessReturn(
domain  tcsite           iSite,
domain  tcorno           iProductionOrder,
domain  tcpono           iPosition,
domain  tcpono           iSequenceNumber,
domain  tcinh.ittp       iTransactionType,
domain  tcqst1           iQuantityToReturn,
domain  tccotp           iReturnOrderType,
domain  tccdis           iReason,
ref     domain  tcibd.sern       iSerialArray() fixed,
ref     domain  tcclot           iLotCodeArray() fixed,
domain  tcclot           iLotCode,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   Process a return quantity on the given Production Order
Production Warehouse Order line.Transaction management is
handled by this Public Interface.
Pre:
Post:
Input:
iSite
Site (Mandatory when the Site concept is active).
iProductionOrder
Production Order - Mandatory.
iPosition
Position - Production Warehouse Order position.
Position 0 always refers to the main item of the order.
iSequenceNumber
Sequence Number - Mandatory.
iTransactionType
Mandatory. The Transaction Type must
have one of the following values:
tcinh.ittp.receipt      - Receipt
tcinh.ittp.issue        - Issue
tcinh.ittp.transfer     - Transfer
iQuantityToReturn
Quantity to return - Mandatory.
iReturnOrderType
Order Type to be used for return processing.
iReason
Reason code
iSerialArray
Array of Serial Numbers.
Pass a filled array (static or dynamic) when the item is
serialized and serial numbers are required; the length
of the array must equal to the Quantity to Return.
Pass an empty array variable when the main item is not
serialized.
E.g. pass the variable dummy.serials, which is defined
as:
domain tcibd.sern dummy.serials(1)
iLotCodeArray
Array of Lot Codes. Usage similar to iSerialArray
Should be provided only if item is both serialized and
lot controlled.
iLotCode
Lot Code.
Should exist if given. Should be provided when item is
only lot controlled.
Output:
oExceptionMessage
The last message if any message is found. If more than
one message is given, these are present in the
oExceptionID.
oExceptionID
An ID that refers to the exception information. Use the
functions in Exception to get all relevant information.
Return: 0       Return quantity is processed.
<> 0    Processing failed
```
