# ProductionOrder.PrintRejects

> Chapter: Chapter 19 Public Interfaces for Job Shop
>
> Group: Public Interfaces for ProductionOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 739-740

```baan
DLL:   tiextsfcapi
This function is available from     2024.10 (KB3511095  ).
Syntax: long ProductionOrder.PrintRejects(
domain  tcsite           iSite,
domain  tcpdno           iProductionOrder,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This Public Interface is used to print Rejects report
(tisfc0403m000). This function makes use of a Processing
Option Set, which can be created via a call to
ProcessingOptionSet.Create(), and cleaned up after use, via a
call to ProcessingOptionSet.Delete().
Pre:    N.A.
Post:   N.A.
Input:  i.site                                - Site for which report must be
printed (Mandatory when the Site
concept is active).
i.production.order                            - Production Order (Optional. Must
be in i.site).
i.processing.option.set                       - A Processing Option Set can be
created via a call to
ProcessingOptionSet.Create().
If 0, then user default/session
default values are applied
(Optional).
Output:
oExceptionMessage      The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID           An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Processing Options have a direct relationship with the form fields
on session Print Rejects (tisfc0403m000) and are not explained in
further detail here. Please refer to the session help for additional
information.
Print Rejects options which are not available as Processing Options
will get defaulted in accordance with the session logic.
NAME                            TYPE                    DEFAULT
ProductionOrderFrom             domain  tcpdno          explained below
ProductionOrderTo               domain  tcpdno          explained below
ProjectFrom                     domain  tccprj          ""
ProjectTo                       domain  tccprj          explained below
CompletionDateFrom              domain  tisfc.utcm      0
CompletionDateTo                domain  tisfc.utcm      explained below
ItemFrom                        domain  tcitem          ""
ItemTo                          domain  tcitem          explained below
SortBy                          domain  tisfc.rjst      tisfc.rjst.item
TaskFrom                        domain  tctano          ""
TaskTo                          domain  tctano          explained below
WorkCenterFrom                  domain  tccwoc          ""
WorkCenterTo                    domain  tccwoc          explained below
MachineFrom                     domain  tirou.mcno      ""
MachineTo                       domain  tirou.mcno      explained below
SuppressNullRejects             domain  tcyesno         tcyesno.no
CompletedOrdersOnly             domain  tcyesno         tcyesno.no
PrintingDevice                  domain  tcmcs.str14     ""
PrintingFileoutPathAndName      domain  tcmcs.str100    ""
Default values:
ProductionOrderFrom               -   If the input variable field iProductionOrder is
given, it will be used as the default value,
otherwise it will be defaulted with blank.
*To               -                   If the "*From" field is provided then "*To"
field will be defaulted with "*From" field,
otherwise the "*To" fields will be defaulted to
their maximum domain value.
For example:
ProductionOrderTo               -     If ProductionOrderFrom field is set, then
ProductionOrderTo field will be the defaulted
with ProductionOrderFrom field, otherwise the
ProductionOrderTo field will be defaulted to
the maximum domain value (i.e. "ZZZZZZZZZ").
TaskFrom and TaskTo values are allowed only when SortBy is
Task(tisfc.rjst.tano) otherwise default values are taken.
WorkCenterFrom and WorkCenterTo values are allowed only when SortBy
is WorkCenter(tisfc.rjst.cwoc) otherwise default values are taken.
MachineFrom and MachineTo values are allowed only when SortBy is
Machine(tisfc.rjst.mcno) otherwise default values are taken.
Output: N.A.
Return: 0                                     - Print Rejects is succesfully.
<> 0                                          - Otherwise.
```
