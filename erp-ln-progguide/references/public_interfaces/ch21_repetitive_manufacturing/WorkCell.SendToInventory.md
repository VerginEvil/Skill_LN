# WorkCell.SendToInventory

> Chapter: Chapter 21 Public Interfaces for Repetitive Manufacturing
>
> Group: Public Interfaces for WorkCell
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 852-852

```baan
DLL:   tiextrptapi
This function is available from 2024.01 (KB2299664).
Syntax: long WorkCell.SendToInventory(
domain  tcsite           iSite,
domain  tccwoc           iWorkCell,
domain  tcorno           iProductionSchedule,
domain  tcitem           iProduct,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   IMPORTANT! This Public Interface cannot be used in parallel
with the Worklist session, as issues may arise. When using this
Public Interface, a user must commit to solely using the Public
Interface logic.
With this Public Interface, completed quantity on the Production
order is posted to deliver to the warehouse blanket order.
The functionality is the same as sending completed quantity to
inventory on the Worklist session (tirpt4602m000).
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iSite                   Site (mandatory if active).
iWorkCell               The workcell (mandatory).
iProductionSchedule     Production Schedule (mandatory).
iProduct                Product (optional).
Output:
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       The reported quantities and / or
status change is processed successfully.
<> 0                    Errors occurred.
```
