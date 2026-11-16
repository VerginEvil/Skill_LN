# InventoryCommitment.AllowedForOrderLine

> Chapter: Chapter 25 Public Interfaces for Warehousing
>
> Group: Public Interfaces for InventoryCommitment
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 962-963

```baan
DLL:   whextinpapi
This function is available from 2023.12 (KB2308183).
Syntax: long InventoryCommitment.AllowedForOrderLine(
domain  whinp.corg       iOrderOrigin,
domain  tcorno           iOrderNumber,
domain  tcpono           iOrderLine,
domain  tcpono           iOrderSequence,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function checks if inventory commitment for the given
order line is allowed.
Commitment can only take place in case no quantity has been
adviced yet. (Status of warehouse order line is 'open')
Input:  iOrderOrigin            - Order Origin (Mandatory)
iOrderNumber            - Order Number (Mandatory)
iOrderLine              - Order Line
iOrderSequence          - Order Sequence
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - No error has been detected.
Inventory Commitment is allowed.
<> 0                    - An Error is detected.
```
