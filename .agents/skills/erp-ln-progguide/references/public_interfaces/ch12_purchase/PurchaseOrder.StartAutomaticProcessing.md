# PurchaseOrder.StartAutomaticProcessing

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 449-449

```baan
DLL:   tdextpurapi
This function is available from 2021.12 (KB2218711).
Syntax: long PurchaseOrder.StartAutomaticProcessing(
domain  tcorno           iPurchaseOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts processing the next purchase order
activities that are set to execute automatically.
This function must not be called within a logical transaction
as this function will have its own transaction handling.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iPurchaseOrder          - Purchase Order (mandatory)
Output: oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Automatic Processing finished or
next activities are not automatic.
<> 0                    - An error occurred
```
