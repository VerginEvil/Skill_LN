# PurchaseOrderReceipt.Confirm

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseOrderReceipt
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 466-467

```baan
DLL:   tdextpurapi
This function is available from     2023.11 (KB2306845  ).
Syntax: long PurchaseOrderReceipt.Confirm(
domain  tcorno           iPurchaseOrder,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderLineSequence,
domain  tcpono           iReceiptSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:
*** Warning ***
This public interface is deprecated.
use:    PurchaseOrderReceipt.ConfirmV2
***************
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
Pre:    LN Application sets retry              -point, so not by caller
Post:   LN Application sets commit/abort transaction, so not by caller
Input:  iPurchaseOrder          Purchase Order (Mandatory)
iOrderLine              Purchase Order Line (Mandatory)
iOrderLineSequence      Purchase Order Line Sequence (Mandatory)
iReceiptSequence        Purchase Order Line Receipt Sequence
(Mandatory)
Output: oExceptionMessage       The last message. This can also be filled
if the return value equals 0.
If more than one  message is given,
these are present in the oExceptionID
oExceptionID            An ID that refers to all error
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       Confirm successfull.
<> 0                    An error occurred
```
