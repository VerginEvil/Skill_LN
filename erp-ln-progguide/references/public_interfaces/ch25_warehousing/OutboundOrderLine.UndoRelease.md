# OutboundOrderLine.UndoRelease

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for OutboundOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 1235-1236

```baan
DLL:   whextinhapi
This function is available from     2025.12 (KB3613235  ).
Syntax: long OutboundOrderLine.UndoRelease(
domain  whinh.oorg       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function undoes the release outbound advice step for the
advice lines related to the given order line which is not yet
picked. The advice is not removed.
This function has its own transaction management. It is not
allowed to call this inside a logical transaction.
When errors occur during the process the errors are visible
in the oExceptionID and the last message is present in
oExceptionMessage.
Pre:    NA
Post:   NA
Input:  iOrderOrigin                          - Order Origin (Mandatory)
iOrderNumber                                  - Order Number (Mandatory)
iOrderLine                                    - Order Line (Optional)
iOrderSequence                                - Order Line Sequence (Optional)
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0: OK, <> 0: Error
```

## Public Interfaces for ReceiptLine

The following functions are available: ReceiptLine.Confirm ReceiptLine.Correct ReceiptLine.CorrectFinalReceipt ReceiptLine.GenerateHandlingUnits ReceiptLine.GenerateHandlingUnitsV2 ReceiptLine.GenerateLots ReceiptLine.GenerateSerials ReceiptLine.GetLanguage ReceiptLine.RemoveHandlingUnits ReceiptLine.Reverse ReceiptLine.Split ReceiptLine.SplitForLotsBatches ReceiptLine.SplitForSerials ReceiptLine.StartAutomaticInboundProcessing ReceiptLine.StartAwaitingDirectMaterialSupply
