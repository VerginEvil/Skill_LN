# EquipmentProcurementOrder.StartAutomaticProcessing

> Chapter: Chapter 12 Public Interfaces for Purchase
>
> Group: Public Interfaces for EquipmentProcurementOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 490-491

```baan
DLL:   tdextpurapi
This function is available from 2025.01 (KB3545450).
Syntax: long EquipmentProcurementOrder.StartAutomaticProcessing(
domain  tcorno           iEquipmentProcurementOrder,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function starts processing the Equipment Procurement
Order activities that are set to execute automatically.
This function must not be called within a logical transaction
as this function has its own transaction handling.
Pre:    There should be no pending transactions before calling this
function.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iEquipmentProcurementOrder
Equipment Procurement Order (Mandatory)
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       - Automatic Processing finished or
next activities are not automatic.
<> 0                    - An error occurred
```
