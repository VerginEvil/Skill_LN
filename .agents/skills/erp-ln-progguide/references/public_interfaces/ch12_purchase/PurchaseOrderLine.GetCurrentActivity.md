# PurchaseOrderLine.GetCurrentActivity

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for PurchaseOrderLine
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 463-463

```baan
DLL:   tdextpurapi
This function is available from 2023.08 (KB2301531).
Syntax: long PurchaseOrderLine.GetCurrentActivity(
domain  tcorno           iPurchaseOrder,
domain  tcpono           iPurchaseOrderLine,
domain  tcpono           iPurchaseOrderLineSequence,
ref     domain  tcmcs.st20m      oCurrentActivity mb,
ref     domain  tcmcs.str60m     oDescription mb,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function retrieves the current activity and associated
(status) description for the given purchase order line.
Pre:    Not Applicable
Post:   Not Applicable
Input:  iPurchaseOrder          - Purchase Order (Mandatory)
iPurchaseOrderLine      - Purchase Order Line (Mandatory)
iPurchaseOrderLineSequence
- Purchase Order Line Sequence (Mandatory)
Output: oCurrentActivity        - Current Activity
oDescription            - Activity (Status) Description
oExceptionMessage       - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Function was executed successful
<> 0                    - An error occurred during execution of
the function.
```
