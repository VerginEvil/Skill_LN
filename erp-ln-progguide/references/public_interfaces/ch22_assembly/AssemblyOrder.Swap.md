# AssemblyOrder.Swap

> Chapter: Chapter 22 Public Interfaces for Assembly
>
> Group: Public Interfaces for AssemblyOrder
>
> Source: Infor LN Public Interfaces & Process Extensions Reference Guide (Cloud), pp. 855-857

```baan
DLL:   tiextascapi
This function is available from     2026.06 (KB3651069  ).
Syntax: long AssemblyOrder.Swap(
domain  tiasln           iAssemblyLine,
domain  tiasl.segm       iLineSegment,
domain  tcorno           iFirstAssemblyOrder,
domain  tcorno           iSecondAssemblyOrder,
long             iProcessingOptionSet,
ref     domain  tcmcs.s999m      oExceptionMessage mb,
ref             long             oExceptionID )
Usage:        Expl.:  Use this Public Interface to swap the assembly orders from their
own existing positions in line sequence.
Swapping means interchanging two orders on a segment. A reschedule
will for instance not be possible if the swap results in too late
arrival of assembly orders in current or next segments.
NOTE:   The user can overrule this by rescheduling, Too late will be
determined by the relative move and the number of random access
places.
This Public Interface reschedules firm and delayed assembly
orders as well and Public Interface will be executed always in
non                      -simulation mode.
Pre:    There should be no pending logical transaction before calling
this function.
Post:   No need to commit or abort the process. Transaction handling
will be done inside Public Interface.
Input:
iAssemblyLine
-                               Assembly Line (Mandatory)
iLineSegment
-                               Assembly Line Segment (Mandatory)
iFirstAssemblyOrder
-                               First Assembly Order (Mandatory)
iSecondAssemblyOrder
-                               Second Assembly Order (Mandatory)
iProcessingOptionSet
-                               Processing Option Set (Optional). If 0, then user
default/session default values are applied.
A Processing Option Set can be created via a call to
ProcessingOptionSet.Create() in DLL tcextextapi. After
the call the option set can be deleted by calling
ProcessingOptionSet.Delete().
Processing Options have a direct relationship with the
form fields on session Reschedule Assembly Orders
(tiasl4220m000) and are not explained in further detail
here. Please refer to the session help for additional
information.
Reschedule Assembly Orders options which are not
available as Processing Options will get defaulted in
accordance with the session logic.
NAME                        TYPE                DEFAULT
IncludeLinkedSegments       Domain tcyesno      tcyesno.no
PrintReport                 Domain tcyesno      tcyesno.no
PrintingDevice              domain tcmcs.str14  ""
PrintingFileoutPathAndName  domain tcmcs.str100 ""
Default Values:
IncludeLinkedSegments
›¼À“ If input variable field "IncludeLinkedSegments" is
given, it will be used as default value. Otherwise,
it will be defaulted with "tcyesno.no". With improved
rescheduling logic, the "IncludeLinkedSegments"
option can be used to also reschedule the order on
segments that are linked to "iLineSegment" via a
'FIFO'                                -buffer. That means: a buffer either of type
FIFO, or of type Random Access, and number of R/A
places is 1.
PrintReport
›¼À“ If input variable field "Print Report" is given, it
will be used as default value. Otherwise, it will be
defaulted with "tcyesno.no". This to to print what is
rescheduled.
Note: In Simulation/Non                      -Simulation modes and Print Report (Y/N),
error messages will be logged to message log and as well
as exception structure.
Output:
oExceptionMessage
-                               The last error message found during the execution of public
interface. If multiple error messages are found, by using
"oExceptionID", messages can be retrieved.
oExceptionID
-                               An ID that refers to the exception information. Use
"Exception" related functions to retrieve related
information.
Return:
0                                     - Success. Assembly Orders are Swapped.
DALHOOKERROR
-                                       Error occurred during Swap process.
```

## Public Interfaces for AssemblyLineStationOrder

The following functions are available: AssemblyLineStationOrder.AllocateParts AssemblyLineStationOrder.ReportFinished AssemblyLineStationOrder.ReportFinishedV2
