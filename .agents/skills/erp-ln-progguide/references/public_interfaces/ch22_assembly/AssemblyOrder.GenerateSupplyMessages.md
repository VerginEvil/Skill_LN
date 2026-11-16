# AssemblyOrder.GenerateSupplyMessages

> Chapter: Chapter 22 Public Interfaces for Assembly
>
> Group: Public Interfaces for AssemblyOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 861-862

```baan
DLL:   tiextascapi
This function is available from 2026.09 (KB3650665).
Syntax: long AssemblyOrder.GenerateSupplyMessages(
domain  tcorno           iAssemblyOrder,
domain  tiasln           iAssemblyLine,
domain  tccwoc           iLineStation,
domain  tcyesno          iGenerateForLateLineStationOrders,
long             iProcessingOptionSet,
ref             boolean          oSomeOrdersProcessed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface generates Supply Messages for Late Line
Station Orders.›¼• This public interface mirrors the behavior of
the session Generate Supply Messages (tiasc8210m100).
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process; that is handled within
the function.
Input:  iAssemblyOrder          Assembly Order.
iAssemblyLine           Assembly Line.
iLineStation            Line Station.
iGenerateForLateLineStationOrders
Control flag for generating supply
messages for Late Line Station Orders.
Default value is Yes in case of empty.
iProcessingOptionSet    Processing Option Set (Optional).
If 0, then user default/session
default values are applied.
A Processing Option Set can be created
via a call to ProcessingOptionSet.Create()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete().
Processing Options have a direct relationship with the form fields
on session Generate Supply Messages (tiasc8210m100) and are not
explained in further detail here. Please refer to the session help for
additional information.
Generate Supply Messages options which are not available as Processing
Options will get defaulted in accordance with the session logic.
NAME                            TYPE            DEFAULT
AssemblyLineFrom        domain  tiasln          ""
AssemblyLineTo          domain  tiasln          explained below
LineStationFrom         domain  tccwoc          ""
LineStationTo           domain  tccwoc          explained below
PlannedStartTimeFrom    domain  tiutcs          0
PlannedStartTimeTo      domain  tiutcs          explained below
AssemblyOrderFrom       domain  tcorno          explained below
AssemblyOrderTo         domain  tcorno          explained below
Default values:
*From -                 If the input variable field i* is given, it
will be used as the default value, otherwise it
will be defaulted with blank.
*To -                   If the "*From" field is provided then "*To"
field will be defaulted with "*From" field,
otherwise the "*To" fields will be defaulted to
their maximum domain value.
For example:
AssemblyOrderFrom -     If the input variable field iAssemblyOrder is
given, it will be used as the default value,
otherwise it will be defaulted with blank.
AssemblyOrderTo -       If AssemblyOrderFrom field is set, then
AssemblyOrderTo field will be the defaulted
with AssemblyOrderFrom field, otherwise the
AssemblyOrderTo field will be defaulted to
the maximum domain value (i.e. "ZZZZZZZZZ").
Output: oSomeOrdersProcessed    True: If one or more Order(s) Processed.
False: Nothing is processed.
oExceptionMessage       The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID            An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                       OK, when multiple orders were selected,
the output variable oSomeOrdersProcessed
can be used to determine whether or not
orders were processed.
When a single order was given via
iAssemblyOrder, the order was processed
successfully.
<> 0                    Otherwise.
When a single order was given via
iAssemblyOrder, the order could not be
processed.
```
