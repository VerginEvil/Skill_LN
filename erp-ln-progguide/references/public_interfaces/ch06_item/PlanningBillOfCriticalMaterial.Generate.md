# PlanningBillOfCriticalMaterial.Generate

> Chapter: Chapter 6 Public Interfaces for Item
>
> Group: Public Interfaces for PlanningBillOfCriticalMaterial
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 240-241

```baan
DLL:   cpextrpdapi
This function is available from     2025.04 (KB3534322  ).
Syntax: long PlanningBillOfCriticalMaterial.Generate(
domain  cpitem           iPlanItem,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl:   This function can be used to Generate Bill of Critical Material.
This Public Interface is similar to Generate Bill of Critical
Material option in session cprpd3220m000. This function makes
use of a Processing Option Set, which can be created via a call
to ProcessingOptionSet.Create(), and cleaned up after use, via a
call to ProcessingOptionSet.Delete(). Transaction management will
be handled by this public interface.
Pre:    N.A.
Post:   N.A.
Input:
iPlanItem               Plan Item
iProcessingOptionSet    A Processing Option Set can be created
via a call to
ProcessingOptionSet.Create().
If 0, then user default/session
default values are applied.
Processing Options have a direct relationship with the form fields
on session Generate Bill of Critical Material (cprpd3220m000) and are not
explained in further detail here. Please refer to the session help for
additional information.
Browse Order Pegging options which are not available as Processing
Options will get defaulted in accordance with the session logic.
NAME                            TYPE                    DEFAULT
PrintingDevice                  domain tcmcs.str14      ""
PrintingFileoutPathAndName      domain tcmcs.str100     ""
ErrorReport                     domain tcyesno          tcyesno.no
ProcessAndErrorReport           domain tcyesno          If ErrorReport is
Yes then
ProcessAndErrorReport
is set No.
Output: oExceptionMessage                     - The last message if any message is
found. If more than one message is
given, these are present in the
oExceptionID.
oExceptionID                                  - An ID that refers to the exception
information. Use the functions in
Exception to get all relevant
information.
Return: 0                                     - Successfully Generated.
<> 0                                          - Otherwise.
```

## Public Interfaces for PlanningBillOfCriticalCapacities

The following functions are available: PlanningBillOfCriticalCapacities.Generate
