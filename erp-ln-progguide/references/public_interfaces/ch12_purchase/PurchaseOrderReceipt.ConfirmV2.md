# PurchaseOrderReceipt.ConfirmV2

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseOrderReceipt
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 467-469

```baan
DLL:   tdextpurapi
This function is available from     2024.04 (KB2326238  ).
Syntax: long PurchaseOrderReceipt.ConfirmV2(
domain  tcorno           iPurchaseOrder,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderLineSequence,
domain  tcpono           iReceiptSequence,
boolean          iHandleTransaction,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:
This function handles the confirm of the given
purchase receipt line.
Received quantity tolerances are checked before starting the
confirm process of the purchase receipt line. This can result
in a warning message that is put on the message stack. This
check does not result in an error that will stop the process.
After that checks are done to determine if it allowed to confirm
the purchase receipt line. If it is not allowed an error will be
given.
Next if modeled so in the system, before the confirm process,
Price Stage blocking functionality is executed and as a result
order line can be blocked (no confirm is done) and the blocking
signal during the blocking process can be set as an
error message on the message stack.
This is not an error situation so function returns with 0.
iReceiptSequence is the sequence from that comes from the
Purchase Actual Receipts (tdpur406) record.
This record must be present and allowed to be confirmed.
Note:
This function does not start the execution of automatic
order steps. A separate Public Interface can be used to
start automatic order steps if necessary:
'PurchaseOrder.StartAutomaticProcessing'
Pre:    Setting a retry              -point depends on 'iHandleTransaction':
true:   No need to set a retry                              -point. This will be taken
care of by the Public Interface.
false:  Caller must set retry                              -point
Post:   Committing/aborting the transaction depends on 'iHandleTransaction':
true:   No need to commit/abort. This will be taken
care of by the Public Interface.
false:  Caller must commit/abort the transaction.
Input:  iPurchaseOrder          Purchase Order (Mandatory)
iOrderLine              Purchase Order Line (Mandatory)
iOrderLineSequence      Purchase Order Line Sequence (Mandatory)
iReceiptSequence        Purchase Order Line Receipt Sequence
(Mandatory)
iHandleTransaction      Handling of transaction management.
Possible values:
-                                               true: Transaction management
will be taken care of by the
Public Interface.
-                                               false:
Caller must handle the transaction
management: set a retry                                                      -point
and commit/abort the transaction.
Output: oExceptionMessage       The last message. This can also be filled
if the return value equals 0.
If more than one  message is given,
these are present in the oExceptionID
oExceptionID            An ID that refers to all error
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Function executed successfully.
Note that if Price Stage blocking
was applicable then the order line
can be blocked and no confirm
has been done.
<> 0                    An error occurred
```
