# WorkCell.RejectProduct

> Chapter: Chapter 21 Public Interfaces for Repetitive Manufacturing
>
> Group: Public Interfaces for WorkCell
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 850-850

```baan
DLL:   tiextrptapi
This function is available from 2024.06 (KB2325441).
Syntax: long WorkCell.RejectProduct(
domain  tccwoc           iWorkCell,
domain  tcutcs           iDate,
domain  tcorno           iProductionSchedule,
domain  tcponl           iProductionScheduleLine,
domain  tcitem           iProduct,
domain  tiqep2           iQuantityRejected,
domain  tcclot           iLotCode,
domain  tcibd.sern       iSerialNumber,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   IMPORTANT! This Public Interface cannot be used in parallel
with the Worklist session, as issues may arise. When using this
Public Interface, a user must commit to solely using the Public
Interface logic.
With this Public Interface, a quantity can be rejected on a
Workcell Shift.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process, that is handled within
the function.
Input:  iWorkcell               The workcell (Mandatory).
iDate                   The date used to determine the shift
If no shift is found at the given date,
the previous shift is used (mandatory).
iProductionSchedule     Production Schedule (Mandatory).
iProductionScheduleLine Production Schedule Line (Optional).
iProduct                Product (Mandatory)
iQuantityRejected       The Quantity to be rejected (Mandatory).
iLotCode                Lot code (Optional)
iSerialNumber           Serial Number (Optional)
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
