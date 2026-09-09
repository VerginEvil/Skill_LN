# AssemblyOrder.Delete

> Chapter: Chapter 22 Public Interfaces for Assembly
>
> Group: Public Interfaces for AssemblyOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 859-860

```baan
DLL:   tiextascapi
This function is available from 2026.01 (KB3614621).
Syntax: long AssemblyOrder.Delete(
domain  tcorno           iAssemblyOrder,
long             iProcessingOptionSet,
ref             boolean          oDataProcessed,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This public interface deletes the assembly orders for which the
work has not started yet.›¼• This public interface mirrors the
behavior of the session Delete Assembly Orders (tiasc2200m000).
Transaction management is handled within the Public Interface.
Pre:    N.A.
Post:   N.A.
Input:  iAssemblyOrder          Assembly Order
iProcessingOptionSet    Processing Option Set (Optional).
If 0, then user default/session
default values are applied.
A Processing Option Set can be created
via a call to ProcessingOptionSet.Create()
in DLL tcextextapi. After the call the
option set can be deleted by calling
ProcessingOptionSet.Delete().
Processing Options have a direct relationship with the form fields
on session Delete Assembly Orders (tiasc2200m000) and are not explained
in further detail here. Please refer to the session help for additional
information.
Delete Assembly Orders options which are not available as Processing
Options will get defaulted in accordance with the session logic.
NAME                        TYPE                DEFAULT
AssemblyOrderFrom           domain tcorno       iAssemblyOrder
AssemblyOrderTo             domain tcorno       explained below
StartDateFrom               domain tiutcd       0
StartDateTo                 domain tiutcd       explained below
PlannedOfflineDateFrom      domain tiutcd       0
PlannedOfflineDateTo        domain tiutcd       explained below
ProductVariantFrom          domain tccpva       0
ProductVariantTo            domain tccpva       explained below
AssemblyLineFrom            domain tiasln       ""
AssemblyLineTo              domain tiasln       explained below
AssemblyStatusFrom          domain tiasc.asst   explained below
AssemblyStatusTo            domain tiasc.asst   explained below
PrintReport                 domain tcyesno      tcyesno.no
PrintingDevice              domain tcmcs.str14  ""
PrintingFileoutPathAndName  domain tcmcs.str100 ""
PrintErrorToReport          domain tcyesno      tcyesno.no
Default values:
AssemblyOrderFrom -     If the input variable field iAssemblyOrder is
given, it will be used as the default value,
otherwise it will be defaulted with blank.
*To -                   If the "*From" field is provided then "*To"
field will be defaulted with "*From" field,
otherwise the "*To" fields will be defaulted to
their maximum domain value.
For example:
AssemblyOrderFrom -     If AssemblyOrderFrom field is set, then
AssemblyOrderTo field will be the defaulted
with AssemblyOrderFrom field, otherwise the
AssemblyOrderTo field will be defaulted to
the maximum domain value (i.e. "ZZZZZZZZZ").
AssemblyStatusFrom -    If AssemblyStatusFrom is given, it will be used
as the default value, otherwise Created
(tiasc.asst.planned) will be defaulted.
AssemblyStatusTo -      If AssemblyStatusTo is given, it will be used
as the default value, otherwise Sequenced
(tiasc.asst.sequenced) will be defaulted.
If PrintErrorToReport is tcyesno.yes, then the error(s) will be printed
in the report. If it is tcyesno.no, then error(s) will be logged in
Message log.
PrintErrorToReport is applicable only if PrintReport is tcyesno.yes.
Output: oDataProcessed          True: Assembly Order(s) Printed.
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
the output variable oDataProcessed can
be used to determine whether or not
orders were deleted.
When a single order was given via
iAssemblyOrder, the order was deleted
successfully.
<> 0                    Otherwise.
When a single order was given via
iAssemblyOrder, the order could not be
deleted.
```
